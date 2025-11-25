import { Plus, Bell } from "lucide-react";
const SubHeader = () => {
  return (
    <div className="flex gap-10  items-center justify-between">
      <div className="flex items-center gap-25">
        <div>
          {" "}
          <h1 className="text-4xl text-white font-semibold m-2">
            Good Morning Alex
          </h1>
          <h3 className="text-md m-2 text-white ">
            Here is how your assistants are planning your day
          </h3>
        </div>
        <div className="bg-gray-900 px-6 py-2 rounded-xl text-gray-400 flex flex-col text-center">
          Today : Tuesday<br></br>
          10:30:45 Am
        </div>
      </div>

      <div className="flex items-center gap-5">
        <Bell className="w-5 h-5 text-yellow-400" />
        <button className="bg-blue-800 m-2 rounded-xl px-8 py-3 text-white flex gap-3 justify-center items-center">
          <Plus className="w-8 h-8" />
          New Task
        </button>
      </div>
    </div>
  );
};
export default SubHeader;
