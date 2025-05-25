import {
  compileScenes,
  generateScene,
  generateSceneDescription,
  mergeScenesAndUpload,
} from "./utils/ai";

import { prisma } from "@repo/db/prismaClient.ts";
import { redisClient } from "./utils/redis";

async function main() {
  console.log(`listening to queue`);

  while (true) {
    try {
      const queueData = await redisClient.BRPOP("generate-video", 0);
      if (!queueData) continue;
      const parsedData = JSON.parse(queueData.element);
      console.log("🚀 ~ Data received", parsedData);
      await generateVideo(parsedData);
    } catch (error) {
      console.log("🚀 ~ main ~ error:", error);
    }
  }
}

main();
async function generateVideo(data: { id: string; prompt: string }) {
  // const data = {
  //   projectId: "123456789",
  //   prompt:
  //     "explain how web works  for beginner in simple terms"}

  const scenesDetail = await generateSceneDescription(data.prompt, data.id);

  // await prisma.project.update({
  //   where: {
  //     id: data.id,
  //   },
  //   data: {
  //     sceneFlow: JSON.stringify(scenesDetail),
  //     totalScene: scenesDetail.length,
  //     status: "GENERATING_SCENES",
  //   },
  // });

  const compileCommands = [];
  for (const sceneConfig of scenesDetail) {
    const scene = await generateScene(sceneConfig, scenesDetail, data.id);
    compileCommands.push(scene);
  }

  // [
  //   {
  //     name: `Scene10RenderingWebPages.py`,
  //     sceneId: "c7532f73-987a-4ca2-a588-bd36a80bf238",
  //     sceneSequence:10,
  //   },
  // ]
  await compileScenes(compileCommands);

  await mergeScenesAndUpload(data.id);
  
  // await prisma.project.update({
  //   where: {
  //     id: data.id,
  //   },
  //   data: {
  //     status: "COMPLETED",
  //   },
  // });
}
