import React from "react";
import PromptComponent from "./_components/prompt";
import History from "./_components/history";

function Dashboard() {
  return (
    <div>
      <PromptComponent />
      <History />
    </div>
  );
}

export default Dashboard;
