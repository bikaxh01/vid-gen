import { SignIn } from "@clerk/nextjs";
import React from "react";

function SignInPage() {
  return (
    <div className=" w-screen h-screen items-center justify-center flex">
      <SignIn />
    </div>
  );
}

export default SignInPage;
