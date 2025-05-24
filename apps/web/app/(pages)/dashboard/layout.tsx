import React, { ReactNode } from "react";
import DashboardNavBar from "./_components/nav";

function Layout({ children }: { children: ReactNode }) {
  return (
    <div>
      <DashboardNavBar />
      <div className=" mt-[3rem] px-44 py-6">{children}</div>
    </div>
  );
}

export default Layout;
