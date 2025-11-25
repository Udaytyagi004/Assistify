import CurrentTask from "./CurrentTask";
import DailyFeed from "./DailyFeed";
import SubHeader from "./SubHeader";
const DashBoard = () => {
  return (
    <div className="absolute left-1/6 w-5/6 p-4 flex flex-col h-screen">
      <SubHeader />
      <div className="h-screen flex">
        <CurrentTask />
        <DailyFeed />
      </div>
    </div>
  );
};
export default DashBoard;
