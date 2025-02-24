// __tests__/regression/ButtonRegression.test.js
import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import Button from '../../components/Button';

test('Verifica se o botão ainda dispara o onClick corretamente', () => {
  const handleClick = jest.fn();
  render(<Button label="Clique" onClick={handleClick} />);
  fireEvent.click(screen.getByText('Clique'));
  expect(handleClick).toHaveBeenCalledTimes(1);
});
