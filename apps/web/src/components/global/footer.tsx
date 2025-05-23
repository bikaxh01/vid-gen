import Link from "next/link";
import React from "react";

function Footer() {
  return (
    <div className="  mt-18 text-gray-400 flex flex-col gap-6">
      <div className=" flex justify-between items-center">
        <Link href={"/"} className=" text-xs ">
          About
        </Link>
        <Link href={"/"} className=" text-xs ">
          Contact
        </Link>
        <Link href={"/"} className=" text-xs ">
          Terms of service
        </Link>
        <Link href={"/"} className=" text-xs ">
          Privacy Policy
        </Link>
      </div>

      <div className=" flex items-center justify-center text-sm">
        Vid-Zen all rights reserved
      </div>
    </div>
  );
}

export default Footer;
