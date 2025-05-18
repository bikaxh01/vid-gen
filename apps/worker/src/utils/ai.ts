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
const execPromise = promisify(exec);
config();
const ai = new GoogleGenAI({ apiKey: GEMINI_API_KEY });

export async function generateScene(
  sceneDetail: SceneConfig,
  scriptDetail: SceneConfig[]
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
  console.log("🚀 ~ scene:", scene);

  // write in file
  const filePath = path.join(
    __dirname,
    "..",
    "..",
    "python",
    `${scene.className}.py`
  );

  await fs.writeFile(filePath, `\n${scene.code}`);
  const compileCommand = `${scene.className}.py`;

  // save each file metadata to db status = code_generated

  return compileCommand;
}

export async function generateSceneDescription(userPrompt: string) {
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

  return scenesDetail;
}

export async function compileScenes(file: any[]) {
  // map on each file and compile
  file.map((fileMetaData: any) => {
    const filePath = path.join(
      __dirname,
      "..",
      "..",
      "python",
      `${fileMetaData.name}`
    );
    // compile each
    exec(`manim -qh ${filePath} `, (error, stdout, stderr) => {
      if (error) {
        console.error(`exec error In code `);

        // fix the code
        fixCode(error, fileMetaData);
        return;
      }
      console.log(`compiled success`);
      if (stderr != "") console.error(`stderr: ${stderr}`);
    });
  });
}

async function fixCode(error: any, fileMetaData: any) {
  let isError = true;
  let count = 1;

  while (isError) {
    if(count >=5 ){
      break;
    }
    isError = await fixCodeAndCompile(error, fileMetaData);
    count++;
   
  }
}

async function fixCodeAndCompile(error: string, fileMetaData: any) {
  const filePath = path.join(
    __dirname,
    "..",
    "..",
    "python",
    `${fileMetaData.name}`
  );
  const currentCode = await fs.readFile(filePath, "utf-8");

  // pass to llm to fix the code
  const response = await ai.models.generateContent({
    model: "gemini-2.5-pro-preview-05-06",
    contents: fixCodePrompt(error, currentCode),
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
      console.log("🚀 ~ exec ~ stderr (warnings?):", stderr);
    }

    console.log("Bug fixed and compiled successfully");
    return false;
  } catch (error) {
    console.log("🚀 ~ fixCodeAndCompile ~ error:", error);
    return true;
  }

  // update db status
  // return is compiled
}
