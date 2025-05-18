import { config } from "dotenv";
import express, { Response, Request } from "express";
import {
  compileScenes,
  generateScene,
  generateSceneDescription,
} from "./utils/ai";
import { PORT } from "./utils/env";
import bodyParser from "body-parser";

config();
const app = express();
app.use(bodyParser.json());

app.post("/generate-video", async (req: Request, res: Response) => {
  // get the user prompt and project id
  const { prompt, userId } = req.body;

  try {
    if (!prompt) {
      res
        .status(401)
        .json({ success: false, message: "Invalid request", data: [] });
      return;
    }

    const scenesDetail = await generateSceneDescription(prompt);

    for (const sceneConfig of scenesDetail) {
      const scene = await generateScene(sceneConfig, scenesDetail);
    }

    res.status(200).json({
      success: true,
      message: "all animations are generated successfully",
      data: [],
    });
  } catch (error) {
    console.log("🚀 ~ app.post ~ error:", error);
    res.status(500).json({
      success: false,
      message: "Error while generating",
      data: [],
    });
  }
});

async function main() {
  const prompt = "generate video on kafka vs redis";
  // const scenesDetail = await generateSceneDescription(prompt);
  // const compileCommands = [];
  // for (const sceneConfig of scenesDetail) {
  //   const scene = await generateScene(sceneConfig, scenesDetail);
  //   compileCommands.push(scene);
  // }

  compileScenes([
    {
      name: "S01_IntroductionKafkaVsRedis.py",
    },
    {
      name: "Scene02SideBySideComparisonSetup.py",
    },
  ]);
}

main();

// app.listen(PORT, () => {
//   console.log(`Running at ${PORT}`);
// });
