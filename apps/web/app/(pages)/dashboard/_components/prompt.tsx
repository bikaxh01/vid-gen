import { Button } from "@/components/ui/button";
import React from "react";

function PromptComponent() {
  return (
    <div className=" flex flex-col justify-between ">
      <div className=" flex items-center justify-center font-semibold">
        Generate Video
      </div>
      <div className=" flex justify-between ">
        <div className="  flex flex-col gap-4 items-start justify-end  w-[40%]">


          <textarea className=" text-sm w-[80%] h-[10rem] bg-muted  rounded-md resize-none p-2  focus:outline-2  placeholder:text-xs" placeholder="Type your Idea"  />

          <div className=" flex items-end  w-full justify-end ">
            <Button className=" text-white ">Generate</Button>
          </div>
        </div>
        <div className=" w-[40%] h-[16rem]  rounded-md">
          video processing here
        </div>
      </div>
    </div>
  );
}

export default PromptComponent;
