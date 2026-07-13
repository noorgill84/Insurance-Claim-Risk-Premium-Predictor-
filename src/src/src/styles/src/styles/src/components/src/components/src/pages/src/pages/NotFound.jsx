```jsx
import { Link } from "react-router-dom";

function NotFound() {
  return (
    <div
      style={{
        height: "80vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
        color: "white"
      }}
    >
      <h1
        style={{
          fontSize: "80px",
          color: "#2563eb"
        }}
      >
        404
      </h1>

      <h2>Page Not Found</h2>

      <p>This page doesn't exist.</p>

      <Link
        to="/dashboard"
        style={{
          marginTop: "20px",
          padding: "12px 25px",
          background: "#2563eb",
          color: "#fff",
          borderRadius: "10px",
          textDecoration: "none"
        }}
      >
        Go to Dashboard
      </Link>
    </div>
  );
}

export default NotFound;
```
