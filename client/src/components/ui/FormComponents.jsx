import React from "react";

function ToggleButton({ itemID, togglePasswordVisibility, showPassword }) {
  return (
    <button
      itemID={itemID}
      type="button"
      onClick={togglePasswordVisibility}
      className="btn btn-success text-muted position-absolute top-50 end-0 translate-middle-y me-2"
    >
      <span
        id="passwordIcon"
        className={showPassword ? "bi bi-eye-slash-fill" : "bi bi-eye-fill"}
      ></span>
    </button>
  );
}

function FormButton({ itemID, text, className }) {
  return (
    <button itemID={itemID} className={className}>
      {text}
    </button>
  );
}

function FormLabel({ text }) {
    return (
        <label className="form-labels">
        {text}
        </label>
    );
}
export { ToggleButton, FormButton, FormLabel };
