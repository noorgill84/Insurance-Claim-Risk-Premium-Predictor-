```jsx
function Settings() {
  return (
    <div className="page-card">
      <h1 className="page-title">Settings</h1>

      <p className="page-subtitle">
        Manage your application settings.
      </p>

      <div
        style={{
          marginTop: "30px",
          display: "grid",
          gap: "20px"
        }}
      >
        <div className="card">
          <h3>Theme</h3>
          <p>Dark Mode Enabled</p>
        </div>

        <div className="card">
          <h3>Notifications</h3>
          <p>Email Notifications Enabled</p>
        </div>

        <div className="card">
          <h3>Model Version</h3>
          <p>Insurance AI Model v1.0</p>
        </div>
      </div>
    </div>
  );
}

export default Settings;
```
