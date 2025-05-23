import Footer from "@/components/global/footer";
import NavBar from "@/components/global/nav";
import React from "react";

function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div>
      <NavBar />
      <div className=" mt-[3rem] px-44 py-6">
        {children}

        <Footer />
      </div>
    </div>
  );
}

export default Layout;
