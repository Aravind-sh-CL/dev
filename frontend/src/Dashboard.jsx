import { useEffect, useState } from "react";

function Dashboard({ onLogin, onRegister }) {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}/dashboard`)
      .then((response) => response.json())
      .then((data) => {
        setMessage(data.message);
      })
      .catch((error) => {
        console.error(error);
        setMessage();
      });
  }, []);

  return (
    <div className="container">
      <div className="login-box">
        <h1>Dashboard</h1>

        <p>{message}</p>

        <button onClick={onLogin}>
          Login
        </button>

        <button onClick={onRegister}>
          Register
        </button>
      </div>
    </div>
  );
}

export default Dashboard;