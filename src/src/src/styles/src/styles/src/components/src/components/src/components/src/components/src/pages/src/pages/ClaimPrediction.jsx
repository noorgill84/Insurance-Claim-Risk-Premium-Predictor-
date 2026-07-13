```jsx
import { useState } from "react";
import axios from "axios";
import "./ClaimPrediction.css";

function ClaimPrediction() {

  const [formData, setFormData] = useState({
    age: "",
    gender: "",
    annual_income: "",
    policy_type: "",
    vehicle_age: "",
    vehicle_value: "",
    driving_experience: "",
    previous_claims: "",
    accident_history: "",
    claim_amount: "",
    policy_duration: "",
    premium_paid: "",
    marital_status: "",
    occupation: "",
    education: "",
    city: "",
    state: "",
    smoking: "",
    alcohol: "",
    health_score: "",
    dependents: "",
    credit_score: "",
    vehicle_type: "",
    engine_capacity: "",
    mileage: ""
  });

  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {

    e.preventDefault();

    setLoading(true);

    try {

      const response = await axios.post(
        "http://127.0.0.1:5000/predict_claim",
        formData
      );

      setPrediction(response.data);

    } catch (error) {

      console.log(error);

      alert("Prediction Failed");

    }

    setLoading(false);

  };

  return (

    <div className="claim-page">

      <h1>Insurance Claim Risk Prediction</h1>

      <p>
        Enter customer details to predict claim risk using the trained AI model.
      </p>

      <form onSubmit={handleSubmit} className="claim-form">

        {Object.keys(formData).map((key) => (

          <div className="form-group" key={key}>

            <label>
              {key.replaceAll("_", " ").toUpperCase()}
            </label>

            <input
              type="text"
              name={key}
              value={formData[key]}
              onChange={handleChange}
              required
            />

          </div>

        ))}

        <button
          className="predict-btn"
          disabled={loading}
        >
          {loading ? "Predicting..." : "Predict Claim Risk"}
        </button>

      </form>

      {prediction && (

        <div className="prediction-result">

          <h2>Prediction Result</h2>

          <h3>

            Claim Risk :
            {" "}
            {prediction.claim_risk}

          </h3>

          <h3>

            Confidence :
            {" "}
            {prediction.confidence}%

          </h3>

        </div>

      )}

    </div>

  );

}

export default ClaimPrediction;
```
