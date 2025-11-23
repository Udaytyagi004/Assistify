import { useDeferredValue } from "react";

const FeatureCard = ({ feat }) => {
  const Icon = feat.icon;
  return (
    <div className="bg-gray-900 text-gray-400 w-1/4 m-4 p-5 ">
      <Icon size={32} strokeWidth={1.5} />
      <h2 className="text-xl mb-5">{feat.name}</h2>
      <p className="text-sm">{feat.description}</p>
    </div>
  );
};
export default FeatureCard;
