import { useState } from "react";
import { set, useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";

import userApi from "../../api/userApi";

// import components
import {
  FormPanel,
  DivInput,
  ToggleButton,
  FormButton,
  FormLabel,
} from "../ui/FormComponents";

function FormRegister() {
  const [form, setForm] = useState({
    username: "",
    password: "",
    email: "",
    name: "",
    last_name: ""
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await userApi.post('/login/user/register/', form);
      navigate("/login");
      console.log(response.data);
    } catch (error) {
      console.error(error.response.data);
    }finally{
      setLoading(false);
    }

  };

  const test = (e) => {
    e.preventDefault();
    console.log("hola");
  };


  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  return (
    <FormPanel>
      <div className="col-md-6 mb-6">
        <img
          src="/img/form-img/logo_proveeagro-bg3.png"
          alt="Logo"
          className="img-fluid"
        />
        <p className="text-body-secondary text-center mt-4 mb-2">
          © Proveeagro 2024
        </p>
      </div>
      <div className="col-md-6">
        <form onSubmit={handleSubmit}>
          <DivInput>
            <i className="bi bi-person-fill text-success me-2"></i>
            <input
              id="username"
              type="text"
              className="form-control"
              name="username"
              placeholder="Tu usuario"
              value={form.username} onChange={handleChange}
              required
            />
            <FormLabel text={"Nuevo usuario"} />
          </DivInput>

          <DivInput>
            <i className="bi bi-lock-fill text-success me-2"></i>
            <input
              id="password"
              type={showPassword ? "text" : "password"}
              className="form-control"
              name="password"
              placeholder="Contraseña"
              value={form.password} onChange={handleChange}
              required
            />
            <ToggleButton
              itemID="passwordButton"
              togglePasswordVisibility={togglePasswordVisibility}
              showPassword={showPassword}
            />
            <FormLabel text={"Nueva contraseña"} />
          </DivInput>
          <DivInput>
            <i className="bi bi-envelope-at-fill text-success me-2"></i>
            <input
              id="email"
              type="text"
              className="form-control"
              name="email"
              placeholder="Tu correo electrónico"
              value={form.email} onChange={handleChange}
              required
            />
            <FormLabel text={"Nuevo correo electrónico"} />
          </DivInput>
          <DivInput>
            <i className="bi bi-person-lines-fill text-success me-2"></i>
            <input
              id="name"
              type="text"
              className="form-control"
              name="name"
              placeholder="Nombre"
              value={form.name} onChange={handleChange}
              required
            />
            <FormLabel text={"Ingresa tu nombre"} />
          </DivInput>
          <DivInput>
            <i className="bi bi-person-lines-fill text-success me-2"></i>
            <input
              id="last_name"
              type="text"
              className="form-control"
              name="last_name"
              placeholder="Apellido"
              value={form.last_name} onChange={handleChange}
              required
            />
            <FormLabel text={"Ingresa tu apellido"} />
          </DivInput>
          <div className="container text-center mt-4 mb-2">
            <FormButton
              type="submit"
              text={loading ? "Cargando..." : "Registrarse"}
              className="btn btn-success"
            />
          </div>

          <div className="text-center pt-4 text-muted">
            ¿Ya tienes una cuenta?
            <Link to="/login" className="text-decoration-none">
              {" Inicia sesión aquí"}
            </Link>
          </div>
        </form>
      </div>
    </FormPanel>
  );
}

export default FormRegister;
