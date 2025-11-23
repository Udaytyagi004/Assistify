import Feature from "../components/Feature";
import Footer from "../components/Footer";
import Hero from "../components/Hero";
import Navbar from "../components/Navbar";

const LandingPage = () => {
  return (
    <div className="bg-black">
      <Navbar />
      <Hero />
      <Feature />
      <Footer />
    </div>
  );
};
export default LandingPage;
