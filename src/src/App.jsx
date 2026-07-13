```jsx
import { Routes, Route, Navigate } from "react-router-dom";

import Sidebar from "./components/Sidebar";
import Navbar from "./components/Navbar";

import Dashboard from "./pages/Dashboard";
import ClaimPrediction from "./pages/ClaimPrediction";
import PremiumPrediction from "./pages/PremiumPrediction";
import Reports from "./pages/Reports";
import Settings from "./pages/Settings";
import NotFound from "./pages/NotFound";

import "./styles/app.css";

function App() {
  return (
    <div className="app">

      <Sidebar />

      <div className="main-content">

        <Navbar />

        <div className="page-content">

          <Routes>

            <Route
              path="/"
              element={<Navigate to="/dashboard" replace />}
            />

            <Route
              path="/dashboard"
              element={<Dashboard />}
            />

            <Route
              path="/claim"
              element={<ClaimPrediction />}
            />

            <Route
              path="/premium"
              element={<PremiumPrediction />}
            />

            <Route
              path="/reports"
              element={<Reports />}
            />

            <Route
              path="/settings"
              element={<Settings />}
            />

            <Route
              path="*"
              element={<NotFound />}
            />

          </Routes>

        </div>

      </div>

    </div>
  );
}

export default App;
```
