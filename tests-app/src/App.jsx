import { useState } from 'react';
import Button from './components/Button';
import Header from './components/Header';
import LoginForm from './components/LoginForm';
import BookManager from './components/BookComponent';

function App() {
  const [count, setCount] = useState(0);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  const increment = () => setCount(count + 1);

  const handleLogin = ({ email, password }) => {
    // Você pode adicionar uma lógica de autenticação aqui
    if (email === 'teste@example.com' && password === '123') {
      setIsAuthenticated(true);
    } else {
      alert('Email ou senha incorretos');
    }
  };

  return (
    <div className="App">
      <Header />
      {!isAuthenticated ? (
        <LoginForm onSubmit={handleLogin} />
      ) : (
        <>
          <p>Contador: {count}</p>
          <Button onClick={increment} label="Incrementar" />
          <div className="App">
            <h1>Gerenciamento de Livros</h1>
            <BookManager />
          </div>
        </>
      )}
    </div>
  );
}

export default App;
