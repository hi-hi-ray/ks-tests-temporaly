import React from 'react';
import { render, fireEvent, screen, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom'; // Matchers personalizados
import App from '../../App'; // O componente que está testando

describe('App Integration Test', () => {
  beforeAll(() => {
    // Mock do alert apenas para este teste
    window.alert = jest.fn();
  });

  test('Mostra o contador somente após o login', async () => {
    render(<App />);

    // Verifica que o contador não é exibido antes do login
    expect(screen.queryByText(/Contador:/)).toBeNull();

    // Faz o login
    fireEvent.change(screen.getByTestId('email-input'), {
      target: { value: 'teste@example.com' }
    });
    fireEvent.change(screen.getByTestId('password-input'), {
      target: { value: '123' }
    });
    fireEvent.click(screen.getByTestId('submit-button'));

    // Verifica se o contador aparece após o login
    await waitFor(() => {
      expect(screen.getByText('Contador: 0')).toBeInTheDocument();
    });
  });

  test('Não mostra o contador com login incorreto', () => {
    render(<App />);

    // Tenta login com credenciais erradas
    fireEvent.change(screen.getByTestId('email-input'), {
      target: { value: 'errado@example.com' }
    });
    fireEvent.change(screen.getByTestId('password-input'), {
      target: { value: '123' }
    });
    fireEvent.click(screen.getByTestId('submit-button'));

    // Verifica que o contador não é exibido com login incorreto
    expect(screen.queryByText(/Contador:/)).toBeNull();
    // Verifica se o alert foi chamado
    expect(window.alert).toHaveBeenCalledWith('Email ou senha incorretos');
  });
});
