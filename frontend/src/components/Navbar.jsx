import { useState, useRef, useEffect } from "react";
import LoginPage from "../pages/LoginPage";

const Navbar = () => {
  const [isClicked, setIsClicked] = useState(false);
  const cardRef = useRef(null);

  useEffect(() => {
    // Close when clicking outside
    const handleClickOutside = (e) => {
      if (cardRef.current && !cardRef.current.contains(e.target)) {
        setIsClicked(false);
      }
    };

    if (isClicked) {
      document.addEventListener("mousedown", handleClickOutside);
    }

    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [isClicked]);

  return (
    <nav className="flex items-center justify-between px-10 py-4 bg-gray-900 shadow-sm sticky top-0 z-50">
      {/* Logo */}
      <div className="text-white text-2xl font-extrabold tracking-tight">
        Assistify
      </div>

      {/* Menu */}
      <ul className="flex gap-8 text-gray-400 font-medium">
        <li className="hover:text-red-400 transition cursor-pointer">
          Product
        </li>
        <li className="hover:text-red-400 transition cursor-pointer">
          Features
        </li>
        <li className="hover:text-red-400 transition cursor-pointer">
          Solution
        </li>
        <li className="hover:text-red-400 transition cursor-pointer">
          Pricing
        </li>
        <li className="hover:text-red-400 transition cursor-pointer">
          Resource
        </li>
      </ul>

      {/* Buttons */}
      <div className="flex items-center gap-4">
        <button
          className="text-gray-300 hover:text-red-400 transition font-medium"
          onClick={() => setIsClicked(true)}
        >
          Login
        </button>
        <button className="px-6 py-2 bg-red-600 hover:bg-red-700 transition text-white rounded-lg font-semibold shadow">
          Get Started
        </button>
      </div>

      {/* Login Card with ref */}
      {isClicked && (
        <>
          {/* Overlay (closes modal on click) */}
          <div
            className="fixed inset-0 bg-black/50 backdrop-blur-sm z-40"
            onClick={() => setIsClicked(false)}
          ></div>

          {/* Card */}
          <div
            ref={cardRef}
            className="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-50"
          >
            <LoginPage />
          </div>
        </>
      )}
    </nav>
  );
};

export default Navbar;
