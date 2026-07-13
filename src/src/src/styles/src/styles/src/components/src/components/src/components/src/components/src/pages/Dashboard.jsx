```jsx
import {
  FaFileInvoiceDollar,
  FaMoneyBillWave,
  FaExclamationTriangle,
  FaRobot,
} from "react-icons/fa";

import {
  ResponsiveContainer,
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  PieChart,
  Pie,
  Cell,
} from "recharts";

const lineData = [
  { month: "Jan", claims: 120 },
  { month: "Feb", claims: 180 },
  { month: "Mar", claims: 140 },
  { month: "Apr", claims: 210 },
  { month: "May", claims: 260 },
  { month: "Jun", claims: 240 },
];

const pieData = [
  { name: "Low Risk", value: 55 },
  { name: "Medium Risk", value: 30 },
  { name: "High Risk", value: 15 },
];

const COLORS = ["#22c55e", "#f59e0b", "#ef4444"];

function Dashboard() {
  return (
    <div className="fade-in">

      <h1 className="page-title">
        Insurance Dashboard
      </h1>

      <p className="page-subtitle">
        AI Powered Insurance Claim Risk & Premium Prediction System
      </p>

      {/* Statistics */}

      <div className="dashboard-grid">

        <div className="dashboard-card">

          <FaFileInvoiceDollar
            size={45}
            color="#3b82f6"
          />

          <h3>Total Claims</h3>

          <div className="dashboard-value">
            2,458
          </div>

          <p>+15% from last month</p>

        </div>

        <div className="dashboard-card">

          <FaMoneyBillWave
            size={45}
            color="#22c55e"
          />

          <h3>Average Premium</h3>

          <div className="dashboard-value">
            ₹18,450
          </div>

          <p>Current yearly average</p>

        </div>

        <div className="dashboard-card">

          <FaExclamationTriangle
            size={45}
            color="#f59e0b"
          />

          <h3>High Risk Policies</h3>

          <div className="dashboard-value">
            128
          </div>

          <p>Needs manual verification</p>

        </div>

        <div className="dashboard-card">

          <FaRobot
            size={45}
            color="#8b5cf6"
          />

          <h3>AI Accuracy</h3>

          <div className="dashboard-value">
            97.8%
          </div>

          <p>Latest trained model</p>

        </div>

      </div>

      {/* Charts */}

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "2fr 1fr",
          gap: "25px",
          marginTop: "30px",
        }}
      >

        <div className="page-card">

          <h2 style={{ marginBottom: "20px" }}>
            Monthly Claims
          </h2>

          <ResponsiveContainer
            width="100%"
            height={350}
          >

            <LineChart data={lineData}>

              <CartesianGrid strokeDasharray="3 3" />

              <XAxis dataKey="month" />

              <YAxis />

              <Tooltip />

              <Line
                type="monotone"
                dataKey="claims"
                stroke="#2563eb"
                strokeWidth={4}
              />

            </LineChart>

          </ResponsiveContainer>

        </div>

        <div className="page-card">

          <h2
            style={{
              textAlign: "center",
              marginBottom: "20px",
            }}
          >
            Risk Distribution
          </h2>

          <ResponsiveContainer
            width="100%"
            height={350}
          >

            <PieChart>

              <Pie
                data={pieData}
                cx="50%"
                cy="50%"
                outerRadius={110}
                dataKey="value"
                label
              >

                {pieData.map((entry, index) => (
                  <Cell
                    key={index}
                    fill={COLORS[index]}
                  />
                ))}

              </Pie>

              <Tooltip />

            </PieChart>

          </ResponsiveContainer>

        </div>

      </div>

      {/* Recent Predictions */}

      <div
        className="page-card"
        style={{ marginTop: "30px" }}
      >

        <h2 style={{ marginBottom: "20px" }}>
          Recent Predictions
        </h2>

        <table>

          <thead>

            <tr>

              <th>Policy ID</th>

              <th>Customer</th>

              <th>Claim Risk</th>

              <th>Premium</th>

              <th>Status</th>

            </tr>

          </thead>

          <tbody>

            <tr>

              <td>PL1001</td>

              <td>Rahul Sharma</td>

              <td>Low</td>

              <td>₹15,200</td>

              <td>Approved</td>

            </tr>

            <tr>

              <td>PL1002</td>

              <td>Simran Kaur</td>

              <td>Medium</td>

              <td>₹22,800</td>

              <td>Pending</td>

            </tr>

            <tr>

              <td>PL1003</td>

              <td>Aman Singh</td>

              <td>High</td>

              <td>₹38,500</td>

              <td>Review</td>

            </tr>

            <tr>

              <td>PL1004</td>

              <td>Priya Verma</td>

              <td>Low</td>

              <td>₹13,900</td>

              <td>Approved</td>

            </tr>

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default Dashboard;
```
