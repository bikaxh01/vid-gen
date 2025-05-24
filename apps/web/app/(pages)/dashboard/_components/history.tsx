import Image from "next/image";
import React from "react";

function History() {
  return (
    <div className=" mt-4">
      <h1 className="  text-2xl font-semibold">History</h1>

      <div className=" flex flex-col gap-3 mt-6">
        <HistoryCard />
        <HistoryCard />
        <HistoryCard />
        <HistoryCard />
        <HistoryCard />
        <HistoryCard />
        <HistoryCard />
        <HistoryCard />
        <HistoryCard />
        <HistoryCard />
        <HistoryCard />
        <HistoryCard />
        <HistoryCard />
        <HistoryCard />
        <HistoryCard />
        <HistoryCard />
        <HistoryCard />
        <HistoryCard />
        <HistoryCard />
        <HistoryCard />
      </div>
    </div>
  );
}

export default History;

function HistoryCard() {
  return (
    <div className=" flex justify-between   ">
      <div className=" w-[50%]   flex flex-col gap-2 rounded-md">
        <p className=" text-xs text-gray-500">2022-10-12</p>
        <h2 className=" text-sm font-semibold ">Title here</h2>
        <p className=" text-xs text-gray-500">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatum
          rerum corporis vero harum porro, exercitationem non perspiciatis et
          praesentium nulla, natus aperiam est iusto recusandae rem consectetur
          officia ad ullam.
        </p>
      </div>
      <div className="  h-[12rem] w-[18rem] rounded-md">
        <Image
          src={
            "https://cdn.statically.io/img/codetheweb.blog/assets/img/posts/css-advanced-background-images/cover.jpg?f=webp&w=1440jpg"
          }
          width={300}
          height={200}
          alt="Image"
          className="  w-full h-full rounded-md"
        />
      </div>
    </div>
  );
}
