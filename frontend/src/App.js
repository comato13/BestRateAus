import React, { useState } from "react";
import axios from "axios";

function App() {
  const [currency, setCurrency] = useState("");
  const [rate, setRate] = useState(null);
  const [timestamp, setTimestamp] = useState(null);

  const fetchRate = async () => {
    const response = await axios.get(`http://127.0.0.1:8000/exchange/${currency}`);
    setRate(response.data.rate);
    setTimestamp(new Date(response.data.last_updated).toLocaleString());
  };

  return (
    <div>
      <h1>Currency Exchange Rate</h1>
      <input
        type="text"
        placeholder="Enter currency (e.g., EUR)"
        onChange={(e) => setCurrency(e.target.value)}
      />
      <button onClick={fetchRate}>Get Rate</button>
      {rate && <p>Exchange Rate: {rate}</p>}
      {timestamp && <p>Last Updated: {timestamp}</p>}
    </div>
  );
}

export default App;