import { useState } from "react";

import Dashboard from "./Dashboard";
import Login from "./Login";
import Register from "./Register";

function App() {
  const [page, setPage] = useState("dashboard");

  if (page === "login") {
  return (
    <Login onBack={() => setPage("dashboard")} />
  );
}

 if (page === "register") {
  return (
    <Register onBack={() => setPage("dashboard")} />
  );
}

  return (
    <Dashboard
      onLogin={() => setPage("login")}
      onRegister={() => setPage("register")}
    />
  );
}

export default App;