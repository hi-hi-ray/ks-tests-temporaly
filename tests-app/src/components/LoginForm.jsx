import  { useState } from 'react';

// eslint-disable-next-line react/prop-types
const LoginForm = ({ onSubmit }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!email || !password) {
      setError('Email e senha são obrigatórios');
    } else {
      setError('');
      onSubmit({ email, password });
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {error && <p data-testid="error-message" style={{ color: 'red' }}>{error}</p>}
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        data-testid="email-input"
      />
      <input
        type="password"
        placeholder="Senha"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        data-testid="password-input"
      />
      <button type="submit" data-testid="submit-button">Login</button>
    </form>
  );
};

export default LoginForm;
