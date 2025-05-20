import { config } from "dotenv";
import express, { Response, Request } from "express";
import {
  compileScenes,
  generateScene,
  generateSceneDescription,
} from "./utils/ai";
import { PORT } from "./utils/env";
import bodyParser from "body-parser";
import { prisma } from "@repo/db/prismaClient.ts";

config();
const app = express();
app.use(bodyParser.json());

// app.post("/generate-video", async (req: Request, res: Response) => {
//   // get the user prompt and project id
//   const { prompt, userId } = req.body;

//   try {
//     if (!prompt) {
//       res
//         .status(401)
//         .json({ success: false, message: "Invalid request", data: [] });
//       return;
//     }

//     const scenesDetail = await generateSceneDescription(prompt);

//     for (const sceneConfig of scenesDetail) {
//       const scene = await generateScene(sceneConfig, scenesDetail);
//     }

//     res.status(200).json({
//       success: true,
//       message: "all animations are generated successfully",
//       data: [],
//     });
//   } catch (error) {
//     console.log("🚀 ~ app.post ~ error:", error);
//     res.status(500).json({
//       success: false,
//       message: "Error while generating",
//       data: [],
//     });
//   }
// });

async function main() {
  const data = {
    projectId: "123456789",
    prompt: "generate video on kafka vs redis generate",
  };

  const scenesDetail = await generateSceneDescription(data.prompt);

  await prisma.project.update({
    where: {
      id: data.projectId,
    },
    data: {
      sceneFlow: JSON.stringify(scenesDetail),
      totalScene: scenesDetail.length,
    },
  });

  const compileCommands = [];
  for (const sceneConfig of scenesDetail) {
    const scene = await generateScene(
      sceneConfig,
      scenesDetail,
      data.projectId
    );
    compileCommands.push(scene);
  }

  const isCompiled = compileScenes(compileCommands);
  // const isCompiled = compileScenes([
  //   {
  //     name: "Scene03KafkaArchitecture.py",
  //     sceneId: "54654654",
  //   },
  //   {
  //     name: "Scene04_Redis_Architecture.py",
  //     sceneId: "54654654",
  //   },
  //   {
  //     name: "Scene05UseCases.py",
  //     sceneId: "54654654",
  //   },
  // ]);
  // merge all scenes
  // upload
  // store link
}

main();

// app.listen(PORT, () => {
//   console.log(`Running at ${PORT}`);
// });
