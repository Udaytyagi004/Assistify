import DashBoard from "../components/DashBoard";
import SideBar from "../components/SideBar";

const HomePage = () => {
  return (
    <div className="bg-black relative h-screen flex">
      <SideBar />
      <DashBoard />
    </div>
  );
};
export default HomePage;
