import { useForm } from "react-hook-form";
import { createFarm } from "../api/farm.api";

export function FarmsFormPage() {
  const { register, handleSubmit, formState: {errors} } = useForm();

  const onSubmit = handleSubmit(async data => {
    const res = await createFarm(data)
    console.log(res)
  });
  return (
    <div>
      <form onSubmit={onSubmit}>
        <input
          type="text"
          placeholder="nombre"
          {...register("name", { required: true })}
        />
        {errors.name && <span>El nombre es requerido</span>}
        <input
          type="text"
          placeholder="dirección"
          {...register("location", { required: true })}
        />
        {errors.location && <span>La dirección es requerida</span>}
        <input
          type="text"
          placeholder="usuario"
          {...register("user", { required: true })}
        />
        {errors.user && <span>El usuario es requerido</span>}
        <input
          type="text"
          placeholder="tipo de finca"
          {...register("farm_type", { required: true })}
        />
        {errors.farm_type && <span>El tipo de finca es requerido</span>}
        <button>Guardar</button>
      </form>
    </div>
  );
}
