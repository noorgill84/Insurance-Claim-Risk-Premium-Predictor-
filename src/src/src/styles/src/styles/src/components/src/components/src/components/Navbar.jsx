```jsx
import { useState, useEffect } from "react";
import {
  FaBell,
  FaMoon,
  FaSun,
  FaSearch,
  FaUserCircle
} from "react-icons/fa";

import "./Navbar.css";

function Navbar() {

  const [darkMode, setDarkMode] = useState(true);
  const [currentTime, setCurrentTime] = useState("");

  useEffect(() => {

    const timer = setInterval(() => {

      const now = new Date();

      setCurrentTime(
        now.toLocaleString("en-IN", {
          dateStyle: "medium",
          timeStyle: "medium",
        })
      );

    }, 1000);

    return () => clearInterval(timer);

  }, []);

  const toggleTheme = () => {
    setDarkMode(!darkMode);
    document.body.classList.toggle("light-mode");
  };

  return (

    <header className="navbar">

      <div className="navbar-left">

        <div className="search-box">

          <FaSearch className="search-icon" />

          <input
            type="text"
            placeholder="Search..."
          />

        </div>

      </div>

      <div className="navbar-right">

        <div className="time-box">

          {currentTime}

        </div>

        <button
          className="icon-btn"
          onClick={toggleTheme}
        >
          {darkMode ? <FaSun /> : <FaMoon />}
        </button>

        <button className="icon-btn">
          <FaBell />
        </button>

        <div className="profile">

          <FaUserCircle className="profile-icon" />

          <div>

            <h4>Admin</h4>

            <small>Insurance Analyst</small>

          </div>

        </div>

      </div>

    </header>

  );
}

export default Navbar;
```
