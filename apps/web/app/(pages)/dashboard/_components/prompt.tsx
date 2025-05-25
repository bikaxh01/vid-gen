"use client";
import { Button } from "@/components/ui/button";
import { useAuth } from "@clerk/nextjs";
import axios from "axios";
import { actionAsyncStorage } from "next/dist/server/app-render/action-async-storage.external";
import React, { useEffect, useState } from "react";

const SERVER_BASE_URL = "http://localhost:3002";

function PromptComponent() {
  const [prompt, setPrompt] = useState("");
  const [pendingProject, setPendingProject] = useState<{ id: string } | null>();
  const [currentStatus, setCurrentStatus] = useState("");
  const { getToken } = useAuth();
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (pendingProject) {
      const getPendingProjectStatus = async () => {
        const res = await axios.get(
          `${SERVER_BASE_URL}/get-project-status?projectId=${pendingProject.id}`
        );

        if (res.data.data.status === "COMPLETED") {
          setCurrentStatus("");
          setPendingProject(null);
          return;
        }

        setCurrentStatus(res.data.data.status);
      };
      const intervalId = setInterval(getPendingProjectStatus, 30000);
      return () => clearInterval(intervalId);
    }
  }, [pendingProject]);

  const handleSubmit = async () => {
    try {
      setLoading(true);
      const token = await getToken();
      const res = await axios.post(
        `${SERVER_BASE_URL}/generate-video`,
        { prompt },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setPendingProject(res.data.data);
    } catch (error) {
      console.log("🚀 ~ handleSubmit ~ error:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className=" flex flex-col justify-between ">
      <div className=" flex items-center justify-center font-semibold">
        Generate Video
      </div>
      <div className=" flex justify-between ">
        <div className="  flex flex-col gap-4 items-start justify-end  w-[40%]">
          <textarea
            className=" text-sm w-[80%] h-[10rem] bg-muted  rounded-md resize-none p-2  focus:outline-2  placeholder:text-xs"
            placeholder="Type your Idea"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
          />

          <div className=" flex items-end  w-full justify-end ">
            <Button
              className=" text-white "
              disabled={loading}
              onClick={handleSubmit}
            >
              Generate
            </Button>
          </div>
        </div>
        {pendingProject && (
          <div className=" w-[40%] h-[16rem] flex items-center justify-center outline  rounded-md">
            {currentStatus || "Generating"}
          </div>
        )}
      </div>
    </div>
  );
}

export default PromptComponent;
