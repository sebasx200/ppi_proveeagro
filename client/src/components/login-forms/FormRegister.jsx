import { useState } from "react";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";
import { toast } from "react-hot-toast";

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
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();
  const [serverError, setServerError] = useState(null);
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const onSubmit = handleSubmit(async (data) => {
    setLoading(true);
    try {
      await userApi.post("/login/user/register/", data);
      toast.success("Usuario registrado correctamente");
      navigate("/login");
    } catch (error) {
      setServerError(error.response.data);
      toast.error("Error al registrar usuario");
    } finally {
      setLoading(false);
    }
  });

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
        <form onSubmit={onSubmit}>
          <div className="panel-heading">
            <h3 className="pt-3 font-weight-bold text-center">Registrarse</h3>
          </div>
          {errors.username && (
            <span className="text-danger">El usuario es requerido</span>
          )}
          <DivInput>
            <i className="bi bi-person-fill text-success me-2"></i>
            <input
              id="username"
              type="text"
              className="form-control"
              name="username"
              placeholder="Tu usuario"
              {...register("username", { required: true })}
            />
            <FormLabel text={"Nuevo usuario"} />
          </DivInput>
          {errors.password && (
            <span className="text-danger">La contraseña es requerida</span>
          )}
          <DivInput>
            <i className="bi bi-lock-fill text-success me-2"></i>
            <input
              id="password"
              type={showPassword ? "text" : "password"}
              className="form-control"
              name="password"
              placeholder="Contraseña"
              {...register("password", { required: true })}
            />
            <ToggleButton
              itemID="passwordButton"
              togglePasswordVisibility={togglePasswordVisibility}
              showPassword={showPassword}
            />
            <FormLabel text={"Nueva contraseña"} />
          </DivInput>
          {errors.email && (
            <span className="text-danger">El correo es requerido</span>
          )}
          <DivInput>
            <i className="bi bi-envelope-at-fill text-success me-2"></i>
            <input
              id="email"
              type="text"
              className="form-control"
              name="email"
              placeholder="Tu correo electrónico"
              {...register("email", { required: true })}
            />
            <FormLabel text={"Nuevo correo electrónico"} />
          </DivInput>
          {errors.name && (
            <span className="text-danger">El nombre es requerido</span>
          )}
          <DivInput>
            <i className="bi bi-person-lines-fill text-success me-2"></i>
            <input
              id="name"
              type="text"
              className="form-control"
              name="name"
              placeholder="Nombre"
              {...register("name", { required: true })}
            />
            <FormLabel text={"Ingresa tu nombre"} />
          </DivInput>
          {errors.last_name && (
            <span className="text-danger">El apellido es requerido</span>
          )}
          <DivInput>
            <i className="bi bi-person-lines-fill text-success me-2"></i>
            <input
              id="last_name"
              type="text"
              className="form-control"
              name="last_name"
              placeholder="Apellido"
              {...register("last_name", { required: true })}
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
          {serverError &&
            Object.keys(serverError).map((key, index) => (
              <div key={index} className="alert alert-danger mt-3" role="alert">
                <p>
                  {key}: {serverError[key]}
                </p>
              </div>
            ))}

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
