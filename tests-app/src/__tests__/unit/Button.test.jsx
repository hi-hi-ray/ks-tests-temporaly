// eslint-disable-next-line no-unused-vars
import React from 'react'; 
import { render, fireEvent, screen } from '@testing-library/react';
import Button from '../../components/Button';

test('Renderiza o botão com o label correto', () => {
  render(<Button label="Clique Aqui" />);
  const button = screen.getByTestId('button');
  expect(button.textContent).toBe('Clique Aqui');
});

test('Executa o onClick ao ser clicado', () => {
  const handleClick = jest.fn();
  render(<Button label="Clique" onClick={handleClick} />);
  fireEvent.click(screen.getByTestId('button'));
  expect(handleClick).toHaveBeenCalledTimes(1);
});
