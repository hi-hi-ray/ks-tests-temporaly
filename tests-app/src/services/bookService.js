import api from '../api/api';

// Adicionar um Livro
export const addBook = async (title, author, isbn) => {
  try {
    const response = await api.post('/books', {
      title,
      author,
      isbn,
    });
    return response.data;
  } catch (error) {
    console.error('Erro ao adicionar livro:', error.response?.data || error.message);
    throw error;
  }
};

// Buscar um Livro pelo ISBN
export const getBookByISBN = async (isbn) => {
  try {
    const response = await api.get(`/books/${isbn}`);
    return response.data;
  } catch (error) {
    console.error('Erro ao buscar livro:', error.response?.data || error.message);
    throw error;
  }
};
