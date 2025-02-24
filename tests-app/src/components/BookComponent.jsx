import React, { useState } from 'react';
import api from '../api/api';

const BookManager = () => {
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  const [isbn, setIsbn] = useState('');
  const [searchIsbn, setSearchIsbn] = useState('');
  const [book, setBook] = useState(null);
  const [error, setError] = useState('');

  const addBook = async () => {
    try {
      await api.post('/books', { title, author, isbn });
      window.alert('Livro adicionado com sucesso!');
      setTitle('');
      setAuthor('');
      setIsbn('');
    } catch (error) {
      console.error(error);
    }
  };


  const searchBook = async () => {
    try {
      const response = await api.get(`/books/${searchIsbn}`);
      setBook(response.data);
      setError('');
    } catch (error) {
      console.log(error)
      setError('Livro não encontrado');
      setBook(null);
    }
  };
  return (
    <div>
      <h2>Adicionar Livro</h2>
      <input
        placeholder="Título"
        type="text"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        data-testid="title-input"
      />
      <input
        placeholder="Autor"
        type="text"
        value={author}
        onChange={(e) => setAuthor(e.target.value)}
        data-testid="author-input"
      />
      <input
        placeholder="ISBN"
        type="text"
        value={isbn}
        onChange={(e) => setIsbn(e.target.value)}
        data-testid="isbn-input-adicionar"
      />
      <button
        onClick={addBook}
        data-testid="add-book-button"
      >
        Adicionar Livro
      </button>

      <h2>Buscar Livro por ISBN</h2>
      <input
        placeholder="ISBN"
        type="text"
        value={searchIsbn}
        onChange={(e) => setSearchIsbn(e.target.value)}
        data-testid="isbn-input-buscar"
      />
      <button
        onClick={searchBook}
        data-testid="search-book-button"
      >
        Buscar
      </button>

      {book && (
        <div>
          <h3>Livro Encontrado:</h3>
          <p>Título: {book.title}</p>
          <p>Autor: {book.author}</p>
          <p>ISBN: {book.isbn}</p>
          <p>Disponível: {book.available ? 'Sim' : 'Não'}</p>
        </div>
      )}

      {error && <p>{error}</p>}
    </div>
  );
};

export default BookManager;
