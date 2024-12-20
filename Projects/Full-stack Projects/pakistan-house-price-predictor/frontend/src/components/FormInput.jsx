import React from 'react';

const FormInput = ({label, name, type, value, onChange}) => (
    <div>
        <label>{label}</label>
        <input
            type={type}
            name={name}
            value={value}
            onChange={onChange}
        />
    </div>
);

export default FormInput;