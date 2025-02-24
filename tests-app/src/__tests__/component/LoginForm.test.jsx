import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import LoginForm from '../../components/LoginForm';

describe('LoginForm Component', () => {
  test('Renderiza corretamente o formulário', () => {
    render(<LoginForm onSubmit={() => {}} />);
    expect(screen.getByPlaceholderText('Email')).toBeInTheDocument();
    expect(screen.getByPlaceholderText('Senha')).toBeInTheDocument();
    expect(screen.getByText('Login')).toBeInTheDocument();
  });

  test('Mostra mensagem de erro quando campos estão vazios', () => {
    render(<LoginForm onSubmit={() => {}} />);
    fireEvent.click(screen.getByTestId('submit-button'));
    expect(screen.getByTestId('error-message')).toBeInTheDocument();
    expect(screen.getByTestId('error-message').textContent).toBe('Email e senha são obrigatórios');
  });

  test('Executa onSubmit com os dados corretos', () => {
    const handleSubmit = jest.fn();
    render(<LoginForm onSubmit={handleSubmit} />);

    fireEvent.change(screen.getByTestId('email-input'), {
      target: { value: 'teste@example.com' }
    });
    fireEvent.change(screen.getByTestId('password-input'), {
      target: { value: '123' }
    });
    fireEvent.click(screen.getByTestId('submit-button'));

    expect(handleSubmit).toHaveBeenCalledTimes(1);
    expect(handleSubmit).toHaveBeenCalledWith({
      email: 'teste@example.com',
      password: '123'
    });
  });
});
