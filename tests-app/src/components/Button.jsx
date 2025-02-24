// src/components/Button.js
// eslint-disable-next-line no-unused-vars
import React from 'react';

// eslint-disable-next-line react/prop-types
const Button = ({ onClick, label }) => (
  <button onClick={onClick} data-testid="button">
    {label}
  </button>
);

export default Button;
