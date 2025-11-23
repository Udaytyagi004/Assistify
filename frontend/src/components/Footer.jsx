const Footer = () => {
  return (
    <footer className="bg-gray-900 text-gray-300 px-10 py-12">
      <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-10">
        {/* Brand Section */}
        <div>
          <h2 className="text-white text-2xl font-bold mb-3">Assistify</h2>
          <p className="text-gray-400 text-sm">
            Your AI-powered assistant for productivity, smart workflows, and
            seamless automation.
          </p>
        </div>

        {/* Product */}
        <div>
          <h3 className="text-white font-semibold mb-3">Product</h3>
          <ul className="space-y-2 text-sm">
            <li className="hover:text-white cursor-pointer">Overview</li>
            <li className="hover:text-white cursor-pointer">Features</li>
            <li className="hover:text-white cursor-pointer">Pricing</li>
            <li className="hover:text-white cursor-pointer">New Releases</li>
          </ul>
        </div>

        {/* Resources */}
        <div>
          <h3 className="text-white font-semibold mb-3">Resources</h3>
          <ul className="space-y-2 text-sm">
            <li className="hover:text-white cursor-pointer">Docs</li>
            <li className="hover:text-white cursor-pointer">API</li>
            <li className="hover:text-white cursor-pointer">Community</li>
            <li className="hover:text-white cursor-pointer">Support</li>
          </ul>
        </div>

        {/* Company */}
        <div>
          <h3 className="text-white font-semibold mb-3">Company</h3>
          <ul className="space-y-2 text-sm">
            <li className="hover:text-white cursor-pointer">About</li>
            <li className="hover:text-white cursor-pointer">Careers</li>
            <li className="hover:text-white cursor-pointer">Blog</li>
            <li className="hover:text-white cursor-pointer">Contact</li>
          </ul>
        </div>
      </div>

      {/* Bottom Section */}
      <div className="border-t border-gray-700 mt-10 pt-6 flex flex-col md:flex-row justify-between items-center text-sm text-gray-500">
        <p>© {new Date().getFullYear()} Assistify. All rights reserved.</p>

        <div className="flex gap-6 mt-4 md:mt-0">
          <p className="hover:text-gray-300 cursor-pointer">Privacy Policy</p>
          <p className="hover:text-gray-300 cursor-pointer">Terms of Service</p>
          <p className="hover:text-gray-300 cursor-pointer">Cookies</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
