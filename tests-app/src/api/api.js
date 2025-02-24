import axios from 'axios';

// Defina o URL base da sua API Flask
const api = axios.create({
  baseURL: 'http://127.0.0.1:5000', // Ajuste a porta conforme necessário
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;