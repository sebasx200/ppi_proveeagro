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
          {...register("address", { required: true })}
        />
        {errors.address && <span>La dirección es requerida</span>}
        <button>Guardar</button>
      </form>
    </div>
  );
}
