```jsx
import { useState } from "react";
import axios from "axios";

function PremiumPrediction() {
  const [data, setData] = useState({
    age: "",
    annual_income: "",
    vehicle_value: "",
    previous_claims: "",
    policy_duration: "",
    health_score: "",
    credit_score: ""
  });

  const [premium, setPremium] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setData({
      ...data,
      [e.target.name]: e.target.value,
    });
  };

  const predictPremium = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const res = await axios.post(
        "http://127.0.0.1:5000/predict_premium",
        data
      );

      setPremium(res.data.predicted_premium);

    } catch (err) {
      alert("Prediction Failed");
      console.error(err);
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: 30 }}>

      <h1>Premium Prediction</h1>

      <form
        onSubmit={predictPremium}
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(2,1fr)",
          gap: 20,
          marginTop: 30
        }}
      >
        {Object.keys(data).map((item) => (
          <input
            key={item}
            type="number"
            name={item}
            placeholder={item.replaceAll("_", " ")}
            value={data[item]}
            onChange={handleChange}
            required
            style={{
              padding: 15,
              borderRadius: 10,
              border: "1px solid #ccc"
            }}
          />
        ))}

        <button
          style={{
            gridColumn: "1/3",
            padding: 15,
            background: "#2563eb",
            color: "#fff",
            border: "none",
            borderRadius: 10,
            cursor: "pointer"
          }}
        >
          {loading ? "Predicting..." : "Predict Premium"}
        </button>

      </form>

      {premium && (
        <div
          style={{
            marginTop: 30,
            padding: 20,
            background: "#16a34a",
            color: "white",
            borderRadius: 12
          }}
        >
          <h2>Predicted Premium</h2>
          <h1>₹ {premium}</h1>
        </div>
      )}

    </div>
  );
}

export default PremiumPrediction;
```
