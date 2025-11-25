import { useState } from "react";
import { menuItems } from "../utils/sidebarList";
import { User } from "lucide-react";

const SideBar = () => {
  const [isActive, setIsActive] = useState("Home");
  return (
    <div className="bg-gray-900 w-1/6 sticky left-0 text-gray-400 h-screen flex flex-col">
      <h1 className="text-2xl font-bold border-b border-gray-800 text-gray-100 shadow-xl p-4">
        Assistify
      </h1>

      <ul className="flex flex-col gap-4 p-4 m-2">
        {menuItems.map((item) => (
          <li
            key={item.name}
            className={`flex items-center gap-3 hover:bg-gray-700 hover:text-white p-2 rounded-lg ${
              isActive === item.name ? "bg-blue-300 text-black" : ""
            }`}
          >
            <item.icon className="w-5 h-5" />
            {item.name}
          </li>
        ))}
      </ul>
      <div className="flex gap-3 absolute bottom-0 p-4 m-4  hover:bg-gray-700 hover:text-white rounded-lg w-fit border-t border-gray-800 shadow-lg">
        <User className="w-5 h-5" />
        Profile
      </div>
    </div>
  );
};
export default SideBar;
