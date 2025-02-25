import React from 'react';
import { render } from '@testing-library/react';
import App from '../../App';

test('Renderiza o App sem erros', () => {
  render(<App />);
});
