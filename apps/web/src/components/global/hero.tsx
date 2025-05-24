import { WandSparkles } from "lucide-react";
import Image from "next/image";
import Link from "next/link";
import React from "react";

function HeroSection() {
  return (
    <div className=" flex flex-col gap-8 p-2 ">
      <div className="bg-[url(https://cdn.statically.io/img/codetheweb.blog/assets/img/posts/css-advanced-background-images/cover.jpg?f=webp&w=1440jpg)] h-[30rem] rounded-md  bg-cover bg-center bg-no-repeat flex justify-center items-center">
        <div className=" flex flex-col items-center  gap-3">
          <div className=" flex flex-col items-center justify-center">
            <h1 className=" font-[1000] text-6xl">
              Create high-quality animated videos
            </h1>
            <h1 className=" font-[1000] text-6xl">with the power of ai</h1>
          </div>
          <p>
            Vid-Zen transforms you idea into animated videos in minutes. No
            experience needed.
          </p>
          <Link
            href={"/dashboard"}
            className=" bg-[#0D80F2]  px-6 py-2  items-center flex font-semibold rounded-md"
          >
            Get started
          </Link>
        </div>
      </div>

      <div>
        <div className=" flex flex-col gap-6">
          <h1 className=" text-2xl font-bold">See Vid-Zen in Action</h1>

          <div className=" flex flex-wrap justify-between">
            <div className="  w-[16rem] h-[12rem] rounded-md">
              <Image
                src={
                  "https://cdn.statically.io/img/codetheweb.blog/assets/img/posts/css-advanced-background-images/cover.jpg?f=webp&w=1440jpg"
                }
                width={300}
                height={200}
                alt="Image"
                className=" h-[8rem] rounded-md"
              />
              <div className=" px-1 py-2">
                <p className=" text-sm font-semibold">Travel vlog</p>
                <p className=" text-xs text-gray-400">
                  Lorem ipsum dolor sit amet consectetur adipisicing elit.
                  Molestiae eum illo accusamus libero recusandae. Consequuntur
                </p>
              </div>
            </div>
            <div className="  w-[16rem] h-[12rem] rounded-md">
              <Image
                src={
                  "https://cdn.statically.io/img/codetheweb.blog/assets/img/posts/css-advanced-background-images/cover.jpg?f=webp&w=1440jpg"
                }
                width={300}
                height={200}
                alt="Image"
                className=" h-[8rem] rounded-md"
              />
              <div className=" px-1 py-2">
                <p className=" text-sm font-semibold">Travel vlog</p>
                <p className=" text-xs text-gray-400">
                  Lorem ipsum dolor sit amet consectetur adipisicing elit.
                  Molestiae eum illo accusamus libero recusandae. Consequuntur
                </p>
              </div>
            </div>
            <div className="  w-[16rem] h-[12rem] rounded-md">
              <Image
                src={
                  "https://cdn.statically.io/img/codetheweb.blog/assets/img/posts/css-advanced-background-images/cover.jpg?f=webp&w=1440jpg"
                }
                width={300}
                height={200}
                alt="Image"
                className=" h-[8rem] rounded-md"
              />
              <div className=" px-1 py-2">
                <p className=" text-sm font-semibold">Travel vlog</p>
                <p className=" text-xs text-gray-400">
                  Lorem ipsum dolor sit amet consectetur adipisicing elit.
                  Molestiae eum illo accusamus libero recusandae. Consequuntur
                </p>
              </div>
            </div>
            <div className="  w-[16rem] h-[12rem] rounded-md">
              <Image
                src={
                  "https://cdn.statically.io/img/codetheweb.blog/assets/img/posts/css-advanced-background-images/cover.jpg?f=webp&w=1440jpg"
                }
                width={300}
                height={200}
                alt="Image"
                className=" h-[8rem] rounded-md"
              />
              <div className=" px-1 py-2">
                <p className=" text-sm font-semibold">Travel vlog</p>
                <p className=" text-xs text-gray-400">
                  Lorem ipsum dolor sit amet consectetur adipisicing elit.
                  Molestiae eum illo accusamus libero recusandae. Consequuntur
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div>
        <div className=" mt-6">
          <div className=" flex gap-8 flex-col">
            <h1 className=" text-2xl font-bold">How Vid-Zen works</h1>

            <div className=" flex flex-col gap-4">
              <h1 className=" text-3xl font-bold">
                Simple Steps to create Amazing Animated Videos
              </h1>
              <p className=" text-xs text-gray-400">
                Vid-Zen makes video creation effortless. Follow these steps to
                bring your ideas to life.
              </p>
            </div>

            <Link
              className=" bg-[#0D80F2]  text-xs px-4 py-2 items-center flex font-semibold w-fit rounded-md"
              href={"/dashboard"}
            >
              Start Creating
            </Link>

            <div className=" flex  justify-between">
              <div className=" flex flex-col px-4 py-4 bg-[#1d1e1f]  w-[16rem] rounded-md   border">
                <div>
                  <WandSparkles className=" size-4 text-gray-400" />
                </div>
                <div className=" flex flex-col gap-1 mt-1.5">
                  <h1 className=" font-semibold">Describe your vision</h1>
                  <p className=" text-xs text-gray-400">
                    Use our intuitive interface to describe the video you want
                    to create. Vid-Zen's AI will generate a draft based on your
                    input.
                  </p>
                </div>
              </div>
              <div className=" flex flex-col px-4 py-4 bg-[#1d1e1f]  w-[16rem] rounded-md   border">
                <div>
                  <WandSparkles className=" size-4 text-gray-400" />
                </div>
                <div className=" flex flex-col gap-1 mt-1.5">
                  <h1 className=" font-semibold">Describe your vision</h1>
                  <p className=" text-xs text-gray-400">
                    Use our intuitive interface to describe the video you want
                    to create. Vid-Zen's AI will generate a draft based on your
                    input.
                  </p>
                </div>
              </div>
              <div className=" flex flex-col px-4 py-4 bg-[#1d1e1f]  w-[16rem] rounded-md   border">
                <div>
                  <WandSparkles className=" size-4 text-gray-400" />
                </div>
                <div className=" flex flex-col gap-1 mt-1.5">
                  <h1 className=" font-semibold">Describe your vision</h1>
                  <p className=" text-xs text-gray-400">
                    Use our intuitive interface to describe the video you want
                    to create. Vid-Zen's AI will generate a draft based on your
                    input.
                  </p>
                </div>
              </div>
              <div className=" flex flex-col px-4 py-4 bg-[#1d1e1f]  w-[16rem] rounded-md   border">
                <div>
                  <WandSparkles className=" size-4 text-gray-400" />
                </div>
                <div className=" flex flex-col gap-1 mt-1.5">
                  <h1 className=" font-semibold">Describe your vision</h1>
                  <p className=" text-xs text-gray-400">
                    Use our intuitive interface to describe the video you want
                    to create. Vid-Zen's AI will generate a draft based on your
                    input.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="  flex flex-col items-center gap-4 mt-7">
        <div>
          <h1 className=" text-3xl font-bold">
            Ready to Transform Your Ideas into Videos?
          </h1>
        </div>
        <Link
          href={"/dashboard"}
          className=" bg-[#0D80F2]  text-xs px-4 py-2 items-center flex font-semibold rounded-md"
        >
          Try Vid-Zen Now
        </Link>
      </div>
    </div>
  );
}

export default HeroSection;
