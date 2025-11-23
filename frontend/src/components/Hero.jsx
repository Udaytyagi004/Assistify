import Lottie from "lottie-react";
import emptyAnimation from "../assets/Assistant.json";

const Hero = () => {
  return (
    <div className="flex justify-around items-center text-gray-400 p-4">
      <div className="flex flex-col w-1/2 p-4">
        <p className="text-5xl font-bold text-gray-300 my-4">
          Offload your busy work to AI and stay focused on real work.
        </p>
        <p className="text-xl">
          Assistify connects to your emial, calender, and tools to automate
          followups , schedule meetings , capture MoM , and keep your day
          running on autopilot
        </p>
      </div>
      <div>
        <Lottie
          animationData={emptyAnimation}
          loop={true}
          className="w-100 h-100"
        />
      </div>
    </div>
  );
};
export default Hero;
