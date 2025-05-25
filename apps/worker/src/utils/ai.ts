import {
  fixCodePrompt,
  generateScenePrompt,
  generateScenesDescriptionPrompt,
} from "./prompts";
import { SceneConfig, SceneProperties } from "./types";
import { GoogleGenAI, Type } from "@google/genai";
import fs from "fs/promises";
import path from "path";
import { exec, spawn } from "child_process";
import { config } from "dotenv";
import { GEMINI_API_KEY } from "./env";
import { promisify } from "util";
import cloudinary from "cloudinary";
import { prisma } from "@repo/db/prismaClient.ts";
import { log } from "console";
const execPromise = promisify(exec);
config();
const ai = new GoogleGenAI({ apiKey: GEMINI_API_KEY });

export async function generateScene(
  sceneDetail: SceneConfig,
  scriptDetail: SceneConfig[],
  projectId: string
) {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-pro-preview-05-06",
    contents: generateScenePrompt(sceneDetail, scriptDetail),
    config: {
      responseMimeType: "application/json",
      responseSchema: {
        type: Type.ARRAY,
        description: "Detail of scene",
        items: {
          type: Type.OBJECT,
          properties: {
            sceneTitle: {
              type: Type.STRING,
              description:
                "The title of the scene, describing the main focus or idea.",
            },
            description: {
              type: Type.STRING,
              description:
                "A detailed explanation of what happens in the scene.",
            },
            className: {
              type: Type.STRING,
              description: "Name of Class that has been created",
            },
            code: {
              type: Type.STRING,
              description: "scene main code of scene",
            },
          },
          required: ["sceneTitle", "description", "code", "className"],
        },
      },
    },
  });

  //@ts-ignore
  const scene: SceneProperties = JSON.parse(response.text)[0];

  // write in file
  const filePath = path.join(
    __dirname,
    "..",
    "..",
    "python",
    `${scene.className}.py`
  );

  const sceneData = await prisma.scene.create({
    data: {
      status: "COMPLETED",
      sequence: sceneDetail.sequence,
      code: scene.code,
      description: scene.description,
      title: scene.sceneTitle,
      projectId,
      className: scene.className,
    },
  });

  await fs.writeFile(filePath, `\n${scene.code}`);
  const metadata = {
    name: `${scene.className}.py`,
    sceneId: sceneData.id,
    sceneSequence: sceneData.sequence,
  };
  console.log(`Scenes ${sceneDetail.sequence} code Completed 🟢🟢`);
  // save each file metadata to db status = code_generated

  return metadata;
}

export async function generateSceneDescription(
  userPrompt: string,
  projectId: string
) {

   await prisma.project.update({
    where: {
      id: projectId,
    },
    data: {
      status: "PLAINNING",
    },
  });

  const response = await ai.models.generateContent({
    model: "gemini-2.0-flash",
    contents: generateScenesDescriptionPrompt(userPrompt),
    config: {
      responseMimeType: "application/json",
      responseSchema: {
        type: Type.ARRAY,
        description:
          "A list of scenes that describe a step-by-step visual breakdown based on the user's prompt.",
        items: {
          type: Type.OBJECT,
          properties: {
            sceneTitle: {
              type: Type.STRING,
              description:
                "The title of the scene, describing the main focus or idea.",
            },
            description: {
              type: Type.STRING,
              description:
                "A detailed explanation of what happens in the scene.",
            },
            visualElements: {
              type: Type.ARRAY,
              description:
                "List of visual elements and components shown in the scene (e.g., diagrams, titles, arrows).",
              items: {
                type: Type.STRING,
              },
            },
            sequence: {
              type: Type.NUMBER,
              description: "The sequence of the scene ",
            },
            colorScheme: {
              type: Type.OBJECT,
              description: "A consistent color scheme used in the scene.",
              properties: {
                background: {
                  type: Type.STRING,
                  description: "The background color (e.g., 'light blue')",
                },
                text: {
                  type: Type.STRING,
                  description: "The primary text color (e.g., 'white')",
                },
                highlights: {
                  type: Type.STRING,
                  description:
                    "The color used for highlighting key elements (e.g., 'yellow')",
                },
              },
              required: ["background", "text", "highlights"],
            },
            animationTypes: {
              type: Type.ARRAY,
              description:
                "List of animation types used in the scene (e.g., Write, FadeIn, Transform).",
              items: {
                type: Type.STRING,
              },
            },
          },
          required: [
            "sceneTitle",
            "description",
            "visualElements",
            "colorScheme",
            "animationTypes",
          ],
        },
      },
    },
  });

 

  //@ts-ignore
  const scenesDetail: SceneConfig[] = JSON.parse(response.text);
  console.log("Scenes Description Completed 🟢");

  return scenesDetail;
}

export async function compileScenes(file: any[]) {
  console.log("compiling scenes 🟢");
  // map on each file and compile
  await Promise.all(
    file.map(async (fileMetaData: any) => {
      const filePath = path.join(
        __dirname,
        "..",
        "..",
        "python",
        `${fileMetaData.name}`
      );
      // compile each

      try {
        const res = await execPromise(`manim -qh ${filePath} `);
        console.log(
          `successfully   compilled scene ${fileMetaData.sceneSequence} 🟢 `
        );
      } catch (error) {
        //fix the code
        console.error(
          `Error while compiling scene ${fileMetaData.sceneSequence} 🔴 Fixing it `
        );
        await fixCode(error, fileMetaData);
      }
    })
  );
}

async function fixCode(error: any, fileMetaData: any) {
  let isError = true;
  //let updatedError = error;
  let count = 1;
  const context: { error: string; code: string }[] = [
    { error: error, code: "" },
  ];
  while (isError) {
    if (count >= 5) {
      console.log("Unable to fix the bug limit reached 🔴");

      break;
    }
    console.log(`Fixing for ${count} time `);

    const { stillError, errorStr, code } = await fixCodeAndCompile(
      context,
      fileMetaData
    );
    isError = stillError;

    //@ts-ignore
    context.push({ error: errorStr, code });
    // updatedError = errorStr;
    count++;
  }
}

async function fixCodeAndCompile(
  errors: { error: string; code: string }[],
  fileMetaData: any
) {
  const filePath = path.join(
    __dirname,
    "..",
    "..",
    "python",
    `${fileMetaData.name}`
  );
  const allErrorString = errors
    .map((obj) => {
      return `{
    error:${obj.error},
    code:${obj.code}
  }`;
    })
    .join(", ");

  const currentCode = await fs.readFile(filePath, "utf-8");
  let stillError = false;

  // pass to llm to fix the code
  const response = await ai.models.generateContent({
    model: "gemini-2.5-pro-preview-05-06",
    //@ts-ignore
    contents: fixCodePrompt(
      //@ts-ignore
      errors[errors.length - 1].error,
      allErrorString,
      currentCode
    ),
    config: {
      responseMimeType: "application/json",
      responseSchema: {
        type: Type.ARRAY,
        description: "fixed code of scene",
        items: {
          type: Type.OBJECT,
          properties: {
            code: {
              type: Type.STRING,
              description: "scene main code of scene",
            },
          },
          required: ["code"],
        },
      },
    },
  });

  //@ts-ignore
  const fixedCode = JSON.parse(response.text)[0].code;

  await fs.writeFile(filePath, `\n${fixedCode}`);

  // compile the code
  try {
    const { stdout, stderr } = await execPromise(`manim -qh ${filePath}`);

    if (stderr) {
      //  console.log("🚀 ~ exec ~ stderr (warnings?):", stderr);
    }

    await prisma.scene.update({
      where: {
        id: fileMetaData.sceneId,
      },
      data: {
        status: "COMPLETED",
      },
    });
    console.log("Bug fixed and compiled successfully");
    return { stillError, errorStr: "" };
  } catch (error) {
    stillError = true;
    return { stillError, errorStr: error, code: fixedCode };
  }
}

cloudinary.v2.config({
  cloud_name: process.env.CLOUDINARY_CLOUD_NAME,
  api_key: process.env.CLOUDINARY_API_KEY,
  api_secret: process.env.CLOUDINARY_API_SECRET,
});

export async function mergeScenesAndUpload(projectId: string) {
  console.log("Merging scenes 🟢");

  // get all scenes path

  try {
    const scenes = await prisma.scene.findMany({
      where: {
        projectId,
      },
      orderBy: {
        sequence: "asc",
      },
      select: {
        id: true,
        className: true,
        sequence: true,
      },
    });

    const finalScenesPath = scenes.map((scene) => {
      const scPath = path.join(
        __dirname,
        "..",
        "..",
        "media",
        "videos",
        `${scene.className}`,
        "1080p60",
        `${scene.className}`
      );
      return `'${scPath}.mp4'`;
    });

    // merge all scenes
    const finalVideoPath = await mergeAllScenes(finalScenesPath);

    const filesToBeUploaded = scenes.map((scene) => {
      const scPath = path.join(
        __dirname,
        "..",
        "..",
        "media",
        "videos",
        `${scene.className}`,
        "1080p60",
        `${scene.className}`
      );
      return { id: scene.id, path: `${scPath}.mp4` };
    });

    const finalPaths = [...filesToBeUploaded, finalVideoPath];

    //  upload all scenes
    const videoUrls = await Promise.all(
      finalPaths.map(async (filepath) => {
        const isFinalVideo = filepath == finalVideoPath;
        const res = await cloudinary.v2.uploader.upload(filepath.path, {
          resource_type: "video",
          folder: `vid-gen/${projectId}`,
          use_filename: true,
        });
        return {
          url: res.secure_url,
          isScene: !isFinalVideo,
          id: filepath.id,
        };
      })
    );

    videoUrls.map(async (sceneUrl) => {
      if (!sceneUrl.isScene) {
        // add to project video
        const project = await prisma.project.update({
          where: {
            id: projectId,
          },
          data: {
            finalVideoUrl: sceneUrl.url,
          },
        });
      } else {
        // add url to scene
        await prisma.scene.update({
          where: {
            id: sceneUrl.id,
          },
          data: {
            url: sceneUrl.url,
          },
        });
      }
    });
  } catch (error) {
    console.log("🚀 ~ mergeScenesAndUpload ~ error:", error);
  }
}

async function mergeAllScenes(filePath: string[]) {
  const ffmpegPath = path.join(__dirname, "..", "..", "final", "concat.txt");
  const finalOutputPath = path.join(
    __dirname,
    "..",
    "..",
    "final",
    "final.mp4"
  );
  const test = filePath.join("\n file ");

  await fs.writeFile(ffmpegPath, ` file ${test}`);
  console.log(`merging using ffmpe`);

  await execPromise(
    `ffmpeg -f concat -safe 0 -i ${ffmpegPath} -c copy ${finalOutputPath}`
  );
  return { path: finalOutputPath, id: "" };
}
