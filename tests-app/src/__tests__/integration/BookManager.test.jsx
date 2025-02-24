import React from 'react';
import { render, fireEvent, screen, waitFor } from '@testing-library/react';
import BookManager from '../../components/BookComponent';
import mockAxios from 'axios';

jest.mock('axios');

describe('Integração: BookManager', () => {
  afterEach(() => {
    jest.clearAllMocks();
  });

  test('Adiciona um livro com sucesso', async () => {
    // Mock da resposta da API ao adicionar um livro
    mockAxios.post.mockResolvedValueOnce({
      data: {
        id: 1,
        title: 'Livro Teste',
        author: 'Autor Teste',
        isbn: '123456789',
        available: true
      }
    });

    render(<BookManager />);

    // Preenche o formulário de adicionar livro
    fireEvent.change(screen.getByTestId('title-input'), {
      target: { value: 'Livro Teste' }
    });
    fireEvent.change(screen.getByTestId('author-input'), {
      target: { value: 'Autor Teste' }
    });
    fireEvent.change(screen.getByTestId('isbn-input-adicionar'), {
      target: { value: '123456789' }
    });

    // Clica no botão de adicionar livro usando data-testid
    fireEvent.click(screen.getByTestId('add-book-button'));

    // Verifica se o alert foi chamado com sucesso
    await waitFor(() => {
      expect(mockAxios.post).toHaveBeenCalledWith('/books', {
        title: 'Livro Teste',
        author: 'Autor Teste',
        isbn: '123456789'
      });
    });
  });

  test('Busca um livro por ISBN com sucesso', async () => {
    // Mock da resposta da API ao buscar um livro
    mockAxios.get.mockResolvedValueOnce({
      data: {
        id: 1,
        title: 'Livro Teste',
        author: 'Autor Teste',
        isbn: '123456789',
        available: true
      }
    });

    render(<BookManager />);

    // Preenche o campo de busca de livro
    fireEvent.change(screen.getByTestId('isbn-input-buscar'), {
      target: { value: '123456789' }
    });

    // Clica no botão de buscar livro usando data-testid
    fireEvent.click(screen.getByTestId('search-book-button'));

    // Verifica se o livro foi exibido corretamente
    await waitFor(() => {
      expect(screen.getByText('Livro Encontrado:')).toBeInTheDocument();
      expect(screen.getByText('Título: Livro Teste')).toBeInTheDocument();
      expect(screen.getByText('Autor: Autor Teste')).toBeInTheDocument();
      expect(screen.getByText('ISBN: 123456789')).toBeInTheDocument();
      expect(screen.getByText('Disponível: Sim')).toBeInTheDocument();
    });
  });

  test('Mostra mensagem de erro ao buscar livro não existente', async () => {
    // Mock da resposta de erro da API ao buscar um livro
    mockAxios.get.mockRejectedValueOnce({
      response: {
        data: {
          error: 'Book not found'
        }
      }
    });

    render(<BookManager />);

    // Preenche o campo de busca de livro
    fireEvent.change(screen.getByTestId('isbn-input-buscar'), {
      target: { value: '000000000' }
    });

    // Clica no botão de buscar livro usando data-testid
    fireEvent.click(screen.getByTestId('search-book-button'));

    // Verifica se a mensagem de erro foi exibida
    await waitFor(() => {
      expect(screen.getByText('Livro não encontrado')).toBeInTheDocument();
    });
  });
});
