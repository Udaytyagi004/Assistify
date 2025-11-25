import { useState } from "react";

const LoginPage = () => {
  const [isLogin, setIsLogin] = useState(true);
  return (
    <div className="flex flex-col gap-4 w-96 p-8 bg-gray-900 rounded-2xl shadow-lg text-white">
      {isLogin && (
        <div className="flex flex-col gap-4  justify-center p-8  text-white">
          <h1 className="text-3xl font-bold text-center">Welcome Back</h1>

          <input
            type="text"
            placeholder="Enter your email"
            className="w-full px-4 py-2 rounded bg-gray-800 border border-gray-700 focus:border-blue-500 focus:outline-none"
          />

          <input
            type="password"
            placeholder="Enter your password"
            className="w-full px-4 py-2 rounded bg-gray-800 border border-gray-700 focus:border-blue-500 focus:outline-none"
          />

          <p className="text-sm text-gray-400 text-center">
            Don't have an account?{" "}
            <span
              className="text-blue-500 cursor-pointer"
              onClick={() => setIsLogin(!isLogin)}
            >
              Sign In
            </span>
          </p>
          <button className="mt-2 w-full py-2 bg-blue-600 rounded-lg hover:bg-blue-700 transition">
            {isLogin ? "Login" : "SignIn"}
          </button>
        </div>
      )}
      {!isLogin && (
        <div className="flex flex-col gap-4 justify-center p-8  text-white">
          <h1 className="text-3xl font-bold text-center">Create an account</h1>
          <input
            type="text"
            placeholder="Enter firstname"
            className="w-full px-4 py-2 rounded bg-gray-800 border border-gray-700 focus:border-blue-500 focus:outline-none"
          />
          <input
            type="text"
            placeholder="Enter lastname"
            className="w-full px-4 py-2 rounded bg-gray-800 border border-gray-700 focus:border-blue-500 focus:outline-none"
          />
          <input
            type="text"
            placeholder="Enter your email"
            className="w-full px-4 py-2 rounded bg-gray-800 border border-gray-700 focus:border-blue-500 focus:outline-none"
          />

          <input
            type="password"
            placeholder="Enter your password"
            className="w-full px-4 py-2 rounded bg-gray-800 border border-gray-700 focus:border-blue-500 focus:outline-none"
          />

          <p className="text-sm text-gray-400 text-center">
            already have an account?{" "}
            <span
              className="text-blue-500 cursor-pointer"
              onClick={() => setIsLogin(!isLogin)}
            >
              Login
            </span>
          </p>
          <button className="mt-2 w-full py-2 bg-blue-600 rounded-lg hover:bg-blue-700 transition">
            {isLogin ? "Login" : "SignIn"}
          </button>
        </div>
      )}
    </div>
  );
};
export default LoginPage;
