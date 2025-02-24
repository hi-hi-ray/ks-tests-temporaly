import React from 'react';
import { render, fireEvent, screen, waitFor } from '@testing-library/react';
import App from '../../App';

describe('App Acceptance Test', () => {
  test('Verifica o fluxo de incremento do contador', async () => {
    render(<App />);

    // Simula o preenchimento do formulário de login
    fireEvent.change(screen.getByTestId('email-input'), {
      target: { value: 'teste@example.com' }
    });
    fireEvent.change(screen.getByTestId('password-input'), {
      target: { value: '123' }
    });
    fireEvent.click(screen.getByTestId('submit-button'));

    // Aguarda o DOM ser atualizado após o login (contador = 0 deve aparecer)
    await waitFor(() => {
      expect(screen.getByText('Contador: 0')).toBeInTheDocument();
    });

    // Agora, após o login bem-sucedido, o botão de incrementar existe
    fireEvent.click(screen.getByTestId('button'));

    // Verifica se o contador foi incrementado
    expect(screen.getByText('Contador: 1')).toBeInTheDocument();
  });
});
