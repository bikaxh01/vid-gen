import Link from "next/link";
import React from "react";

function NavBar() {
  return (
    <div className="  h-[3rem]   px-20 py-2 flex  border-b-1 fixed top-0 left-0 w-full bg-background border-gray-500 justify-between">
      <div>
        <h2 className=" text-2xl font-semibold">Vid-Zen</h2>
      </div>

      <div className=" gap-4 flex items-center justify-center">
        <Link href={"/"} className=" text-xs font-semibold">
          Home
        </Link>
        <Link href={"/"} className=" text-xs font-semibold">
          Features
        </Link>
        <Link href={"/"} className=" text-xs font-semibold">
          Pricing
        </Link>
        <Link href={"/"} className=" text-xs font-semibold">
          Resources
        </Link>
        <Link
          href={"/sign-in"}
          className=" bg-[#0D80F2]  text-xs px-4 py-2 items-center flex font-semibold rounded-md"
        >
          Sign-In
        </Link>
      </div>
    </div>
  );
}

export default NavBar;
