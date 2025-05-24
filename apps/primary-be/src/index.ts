import { prisma } from "@repo/db/prismaClient.ts";
import "dotenv/config";
import { config } from "dotenv";
import express, { Request, response, Response } from "express";
import { Webhook, WebhookUnbrandedRequiredHeaders } from "svix";
import {
  clerkClient,
  clerkMiddleware,
  getAuth,
  requireAuth,
} from "@clerk/express";
import { redisClient } from "./config/redis";
import bodyParser from "body-parser";
import { verifyWebhook } from "@clerk/express/webhooks";
config();

const app = express();

app.use(bodyParser.json());
app.use(clerkMiddleware());

app.get("/", (req: Request, res: Response) => {
  res.json({
    message: "Hello world",
  });
});

app.get("/protected", requireAuth(), async (req: Request, res: Response) => {
  const { userId } = getAuth(req);
  console.log("🚀 ~ app.get ~ userId:", userId);

  if (!userId) {
    res.json("Unaunthticated");
    return;
  }

  const user = await clerkClient.users.getUser(userId);

  res.json({ user });
});

app.post(
  "/generate-video",
  requireAuth(),
  async (req: Request, res: Response) => {
    try {
      const { userId } = getAuth(req);
      const { prompt } = req.body;

      // create project

      if (!userId) {
        res.json("Unauthentiacted");
        return;
      }

      const projectDetail = await prisma.project.create({
        data: {
          userId,
          prompt,
          status: "QUEUED",
        },
        select: {
          id: true,
          prompt: true,
        },
      });

      // push to queue
      await redisClient.lPush("generate-video", JSON.stringify(projectDetail));

      res.json({
        message: "Pushed to queue",
        data: projectDetail,
      });
    } catch (error) {
      console.log("🚀 ~ error:", error);
      res.status(500).json({
        message: "Internal serer error",
      });
    }
  }
);

app.post("/webhook-clerk", async (req: Request, res: Response) => {
  try {
    const webhookSecret = process.env.CLERK_WEBHOOK_SIGNING_SECRET as string;
    const payload = req.body;

    const header = {
      "svix-id": req.headers["svix-id"],
      "svix-timestamp": req.headers["svix-timestamp"],
      "svix-signature": req.headers["svix-signature"],
    };

    if (
      !header["svix-id"] ||
      !header["svix-signature"] ||
      !header["svix-timestamp"]
    ) {
      res.status(400).send("Error verifying webhook");
      return;
    }
    
    const wh = new Webhook(webhookSecret);
    
    //@ts-ignore
    const data = wh.verify(JSON.stringify(payload), header);
   

    await prisma.user.create({
      data: {
        id: payload.data.id,
        email: payload.data.email_addresses[0].email_address,
        fullName: `${payload.data.first_name} ${payload.data.last_name}`,
      },
    });

    res.send("Webhook received");
  } catch (err) {
    console.error("Error verifying webhook:", err);
    res.status(400).send("Error verifying webhook");
  }
});

const port = process.env.PORT;

app.listen(port, () => {
  console.log(`started at ${port}`);
});
