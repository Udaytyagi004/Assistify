const Navbar = () => {
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

      {/* Action Buttons */}
      <div className="flex items-center gap-4">
        <button className="text-gray-300 hover:text-red-400 transition font-medium">
          Login
        </button>
        <button className="px-6 py-2 bg-red-600 hover:bg-red-700 transition text-white rounded-lg font-semibold shadow">
          Get Started
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
