```jsx
import { NavLink } from "react-router-dom";
import {
  FaChartLine,
  FaMoneyCheckAlt,
  FaFileInvoiceDollar,
  FaChartPie,
  FaCog,
  FaShieldAlt
} from "react-icons/fa";

import "./Sidebar.css";

function Sidebar() {
  const menuItems = [
    {
      title: "Dashboard",
      icon: <FaChartLine />,
      path: "/dashboard",
    },
    {
      title: "Claim Prediction",
      icon: <FaFileInvoiceDollar />,
      path: "/claim",
    },
    {
      title: "Premium Prediction",
      icon: <FaMoneyCheckAlt />,
      path: "/premium",
    },
    {
      title: "Reports",
      icon: <FaChartPie />,
      path: "/reports",
    },
    {
      title: "Settings",
      icon: <FaCog />,
      path: "/settings",
    },
  ];

  return (
    <aside className="sidebar">

      <div className="logo-section">

        <div className="logo-icon">
          <FaShieldAlt />
        </div>

        <div>
          <h2>InsureAI</h2>
          <span>Prediction System</span>
        </div>

      </div>

      <nav className="sidebar-menu">

        {menuItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) =>
              isActive ? "menu-item active" : "menu-item"
            }
          >
            <span className="icon">{item.icon}</span>

            <span>{item.title}</span>
          </NavLink>
        ))}

      </nav>

      <div className="sidebar-footer">

        <p>Insurance Claim Risk</p>

        <small>AI & ML Dashboard</small>

      </div>

    </aside>
  );
}

export default Sidebar;
```
