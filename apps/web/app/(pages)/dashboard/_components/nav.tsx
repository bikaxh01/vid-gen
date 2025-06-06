import { UserButton } from "@clerk/nextjs";
import Link from "next/link";
import React from "react";

function DashboardNavBar() {
  return (
    <div className="  h-[3rem]   px-20 py-2 flex  border-b-1 fixed top-0 left-0 w-full bg-background border-gray-500 justify-between">
      <div>
        <h2 className=" text-2xl font-semibold">Vid-Zen</h2>
      </div>

      <div className=" gap-4 flex items-center justify-center">
        <UserButton />
      </div>
    </div>
  );
}

export default DashboardNavBar;
