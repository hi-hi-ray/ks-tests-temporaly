// src/__tests__/integration/BookManager.test.jsx
import React from 'react';
import { render, fireEvent, screen, waitFor } from '@testing-library/react';
import mockAxios from 'axios';
import BookManager from '../../components/BookComponent';

// Mocka a instância de axios
jest.mock('axios');

describe('Integração: BookManager', () => {
  afterEach(() => {
    jest.clearAllMocks();
  });

  test('Adiciona um livro com sucesso', async () => {
    // Mock da resposta do POST
    mockAxios.post.mockResolvedValueOnce({
      data: {
        id: 1,
        title: 'Livro Teste',
        author: 'Autor Teste',
        isbn: '123456789',
        available: true,
      },
    });

    render(<BookManager />);

    // Preenche o formulário
    fireEvent.change(screen.getByTestId('title-input'), {
      target: { value: 'Livro Teste' },
    });
    fireEvent.change(screen.getByTestId('author-input'), {
      target: { value: 'Autor Teste' },
    });
    fireEvent.change(screen.getByTestId('isbn-input-adicionar'), {
      target: { value: '123456789' },
    });

    // Clica no botão para adicionar
    fireEvent.click(screen.getByTestId('add-book-button'));

    // Aguarda e verifica se o mock foi chamado corretamente
    await waitFor(() => {
      expect(mockAxios.post).toHaveBeenCalledWith('/books', {
        title: 'Livro Teste',
        author: 'Autor Teste',
        isbn: '123456789',
      });
    });
  });

  test('Busca um livro por ISBN com sucesso', async () => {
    mockAxios.get.mockResolvedValueOnce({
      data: {
        id: 1,
        title: 'Livro Teste',
        author: 'Autor Teste',
        isbn: '123456789',
        available: true,
      },
    });

    render(<BookManager />);

    fireEvent.change(screen.getByTestId('isbn-input-buscar'), {
      target: { value: '123456789' },
    });

    fireEvent.click(screen.getByTestId('search-book-button'));

    await waitFor(() => {
      expect(screen.getByText('Livro Encontrado:')).toBeInTheDocument();
      expect(screen.getByText('Título: Livro Teste')).toBeInTheDocument();
      expect(screen.getByText('Autor: Autor Teste')).toBeInTheDocument();
      expect(screen.getByText('ISBN: 123456789')).toBeInTheDocument();
      expect(screen.getByText('Disponível: Sim')).toBeInTheDocument();
    });
  });
});
