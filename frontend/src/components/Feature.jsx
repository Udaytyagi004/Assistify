import { featuresList } from "../utils/featuresList";
import FeatureCard from "./FeatureCard";
const Feature = () => {
  return (
    <div className="text-gray-400 mx-15 p-12  border-gray-300">
      <h2 className="text-2xl  mb-2 font-bold">
        AI Agents that work like a chef to staff
      </h2>
      <p className="mb-5">
        Each agent is designed for a specific workflow and works <br></br>
        safely inside your existing tools and permissions.
      </p>
      <div className="flex flex-wrap  gap-12  justify-between">
        {featuresList.map((feat, index) => (
          <FeatureCard key={index} feat={feat} />
        ))}
      </div>
    </div>
  );
};
export default Feature;
