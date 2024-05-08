import { useState } from "react";
import userApi from "../../api/userApi";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../../constants";

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
    <div classNameName="container">
      <div className="row">
        <div className="offset-md-2 col-lg-5 col-md-7 offset-lg-4 offset-md-3">
          <div className="panel border bg-white">
            <div className="panel-heading">
              <img
                className="h-25 w-25"
                src="/img/form-img/logo_proveeagro.png"
                alt="Proveeagro"
              />
              <h2 className="pt-3 font-weight-bold">Iniciar sesión</h2>
            </div>
            <div className="panel-body p-3">
              <form onSubmit={handleSubmit}>
                <div className="form-floating mb-2">
                  <i className="bi bi-person-fill text-primary me-2"></i>
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
                  <label for="floatingInput" className="form-labels">
                    Usuario
                  </label>
                </div>

                <div className="form-floating mb-2">
                  <i className="bi bi-lock-fill text-primary me-2"></i>
                  <input
                    id="password"
                    type={showPassword ? 'text' : 'password'}
                    className="form-control"
                    name="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Contraseña"
                    required
                  />
                  <label for="floatingPassword" className="form-labels">
                    Contraseña
                  </label>
                  <button
                    type="button"
                    id="togglePasswordButton"
                    onClick={togglePasswordVisibility}
                    className="btn bg-white text-muted position-absolute top-50 end-0 translate-middle-y me-2"
                  >
                    <span
                      id="passwordIcon"
                      className={showPassword ? 'bi bi-eye-slash-fill' : 'bi bi-eye-fill'}
                    ></span>
                  </button>
                </div>
                <div className="form-inline">
                  <input type="checkbox" name="remember" id="remember" />
                  <label for="remember" className="text-muted">
                    Recordar
                  </label>
                  <a href="#" id="forgot" className="font-weight-bold">
                    ¿Olvidaste tu contraseña?
                  </a>
                </div>
                <div className="container text-center mt-4 mb-2">
                  <button className="btn btn-primary" type="submit">
                    {loading ? "Cargando..." : "Iniciar Sesión"}
                  </button>
                </div>

                <div className="text-center pt-4 text-muted">
                  ¿No tienes una cuenta?{" "}
                  <a href="/register">Regístrate aquí</a>
                </div>
                <p className="text-body-secondary mt-4 mb-2">
                  © Proveeagro 2024
                </p>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default FormLogin;
