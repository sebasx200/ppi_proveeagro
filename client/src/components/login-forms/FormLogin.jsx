import { useState } from "react";
import userApi from "../../api/userApi";
import { useNavigate } from "react-router-dom";
import { Link } from 'react-router-dom';
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../../constants";

// import components
import { ToggleButton, FormButton, FormLabel } from "../ui/FormComponents";

import "../../styles/login.css";

function FormLogin({ route }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  const handleSubmit = async (e) => {
    setLoading(true);
    e.preventDefault();

    try {
      const res = await userApi.post(route, { username, password });

      localStorage.setItem(ACCESS_TOKEN, res.data.access);
      localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
      navigate("/");
    } catch (error) {
      alert(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="panel">
        <div className="form-container">
          <img
            src="/img/form-img/logo_proveeagro-bg3.png"
            alt="Proveeagro"
          />
          <form onSubmit={handleSubmit}>
            <h2 className="text-center">Iniciar Sesión</h2>
            <div className="form-floating mb-2">
              <i className="bi bi-person-fill text-success me-2"></i>
              <input
                id="username"
                type="text"
                className="form-control"
                name="username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Tu usuario"
                required
              />
              <FormLabel text={"Usuario"} />
            </div>

            <div className="form-floating mb-2">
              <i className="bi bi-lock-fill text-success me-2"></i>
              <input
                id="password"
                type={showPassword ? "text" : "password"}
                className="form-control"
                name="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Contraseña"
                required
              />
              <FormLabel text={"Contraseña"} />
              <ToggleButton
                itemID="passwordButton"
                togglePasswordVisibility={togglePasswordVisibility}
                showPassword={showPassword}
              />
            </div>
            <div className="form-inline">
              <input type="checkbox" name="remember" id="remember" />
              <label className="text-muted">Recordar</label>
              <Link to="#" id="forgot" className="font-weight-bold">
                ¿Olvidaste tu contraseña?
              </Link>
            </div>
            <div className="container text-center mt-4 mb-2">
              <FormButton
                itemID="loginButton"
                text={loading ? "Cargando..." : "Ingresar"}
                className="btn btn-success"
              />
            </div>

            <div className="text-center pt-4 text-muted">
              ¿No tienes una cuenta?
              <Link to="/register" className="text-decoration-none">
                {" Regístrate aquí"}
              </Link>
            </div>
            <p className="text-body-secondary mt-4 mb-2">© Proveeagro 2024</p>
          </form>
        </div>
      </div>
  );
}

export default FormLogin;
