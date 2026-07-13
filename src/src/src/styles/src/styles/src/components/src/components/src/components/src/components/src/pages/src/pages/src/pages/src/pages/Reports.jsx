```jsx
function Reports() {

  const reports = [
    {
      id: 1,
      customer: "Rahul Sharma",
      claim: "Low",
      premium: "₹15,200",
      status: "Approved"
    },
    {
      id: 2,
      customer: "Simran Kaur",
      claim: "Medium",
      premium: "₹22,800",
      status: "Pending"
    },
    {
      id: 3,
      customer: "Aman Singh",
      claim: "High",
      premium: "₹38,500",
      status: "Review"
    },
    {
      id: 4,
      customer: "Priya Verma",
      claim: "Low",
      premium: "₹13,900",
      status: "Approved"
    }
  ];

  return (
    <div style={{ padding: 30 }}>

      <h1>Prediction Reports</h1>

      <table
        style={{
          width: "100%",
          marginTop: 30,
          borderCollapse: "collapse"
        }}
      >
        <thead>

          <tr style={{ background: "#2563eb", color: "white" }}>
            <th style={{ padding: 15 }}>ID</th>
            <th>Customer</th>
            <th>Claim Risk</th>
            <th>Premium</th>
            <th>Status</th>
          </tr>

        </thead>

        <tbody>

          {reports.map((item) => (

            <tr key={item.id} style={{ textAlign: "center" }}>

              <td style={{ padding: 15 }}>{item.id}</td>
              <td>{item.customer}</td>
              <td>{item.claim}</td>
              <td>{item.premium}</td>
              <td>{item.status}</td>

            </tr>

          ))}

        </tbody>

      </table>

      <div
        style={{
          marginTop: 40,
          padding: 20,
          background: "#1e293b",
          borderRadius: 12,
          color: "white"
        }}
      >
        <h2>System Summary</h2>

        <p>Total Predictions: 2458</p>
        <p>Approved Claims: 1984</p>
        <p>Pending Claims: 328</p>
        <p>Rejected Claims: 146</p>

        <button
          style={{
            marginTop: 20,
            padding: "12px 25px",
            background: "#16a34a",
            color: "white",
            border: "none",
            borderRadius: 8,
            cursor: "pointer"
          }}
        >
          Download Report
        </button>

      </div>

    </div>
  );
}

export default Reports;
```
