import { useState } from "react";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";

import userApi from "../../api/userApi";

function FormRegister({ route }) {
  
  return (
    <div>
      Formulario de registro
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Usuario"
          required
          {...register("username", { required: true })}
        />

        <input
          type="password"
          placeholder="Contraseña"
          required
          {...register("password", { required: true })}
        />

        <input
          type="email"
          placeholder="Correo"
          required
          {...register("email", { required: true })}
        />
        <input
          type="text"
          placeholder="Nombre"
          required
          {...register("name", { required: true })}
        />
        <input
          type="text"
          placeholder="Apellido"
          required
          {...register("lastname", { required: true })}
        />
        <button type="submit">Registrarse</button>
      </form>
    </div>
  );
}

export default FormRegister;
