describe('App E2E Test', () => {
  beforeEach(() => {
    // Acessa a URL base definida no cypress.config.js
    cy.visit('/');
  });

  it('Deve fazer login com sucesso e incrementar o contador', () => {
    // Aguarda o campo de email aparecer antes de interagir
    cy.get('[data-testid="email-input"]', { timeout: 10000 }).should('be.visible');
    cy.get('[data-testid="email-input"]').type('teste@example.com');
    cy.get('[data-testid="password-input"]').type('123');

    // Clica no botão de login
    cy.get('[data-testid="submit-button"]').click();

    // Verifica se o contador aparece após o login
    cy.contains('Contador: 0').should('be.visible');

    // Clica no botão de incrementar
    cy.get('[data-testid="button"]').click();

    // Verifica se o contador foi incrementado
    cy.contains('Contador: 1').should('be.visible');
  });

  it('Deve mostrar mensagem de erro com credenciais inválidas', () => {
    // Aguarda o campo de email aparecer antes de interagir
    cy.get('[data-testid="email-input"]', { timeout: 10000 }).should('be.visible');
    cy.get('[data-testid="email-input"]').type('errado@example.com');
    cy.get('[data-testid="password-input"]').type('senhaerrada');

    // Intercepta o alert para verificar se foi chamado
    cy.on('window:alert', (str) => {
      expect(str).to.equal('Email ou senha incorretos');
    });

    // Clica no botão de login
    cy.get('[data-testid="submit-button"]').click();

    // Verifica se o contador não aparece
    cy.contains('Contador:').should('not.exist');
  });
});

describe('BookManager E2E Test', () => {
  beforeEach(() => {
    // Visita a aplicação e faz o login
    cy.visit('/');
    cy.get('[data-testid="email-input"]').type('teste@example.com');
    cy.get('[data-testid="password-input"]').type('123');
    cy.get('[data-testid="submit-button"]').click();
  });

  it('Limpa o banco e depois cria um livro com sucesso', () => {
    // 1) Limpa a tabela de livros na API
    cy.request('DELETE', 'http://127.0.0.1:5000/books').then((resp) => {
      expect(resp.status).to.eq(200); // Verifica se limpou com sucesso
    });

    // 2) Intercepta a requisição POST /books
    cy.intercept({
      method: 'POST',
      url: 'http://127.0.0.1:5000/books'
    }).as('createBook');

    // 3) Preenche os campos de adicionar livro
    cy.get('[data-testid="title-input"]').type('Livro E2E');
    cy.get('[data-testid="author-input"]').type('Autor E2E');
    cy.get('[data-testid="isbn-input-adicionar"]').type('123456789');

    // 4) Stub do alert para verificar a mensagem
    cy.window().then((win) => {
      cy.stub(win, 'alert').as('alerta');
    });

    // 5) Clica no botão de adicionar livro
    cy.get('[data-testid="add-book-button"]').click();

    // 6) Aguarda a requisição real para a API e verifica o status
    cy.wait('@createBook').then((intercept) => {
      // Ajuste para acessar o status code corretamente
      expect(intercept.response.statusCode).to.eq(201);
      // Verifica se o alert foi chamado com a mensagem correta
      cy.get('@alerta').should('have.been.calledWith', 'Livro adicionado com sucesso!');
    });


    cy.intercept('GET', 'http://127.0.0.1:5000/books/123456789').as('getBook');

    // Preenche o campo de busca
    cy.get('[data-testid="isbn-input-buscar"]').type('123456789');

    // Clica no botão de buscar
    cy.get('[data-testid="search-book-button"]').click();

    // Espera a resposta do GET
    cy.wait('@getBook').then((interception) => {
      expect(interception.response.statusCode).to.eq(200);
    });

    // Verifica se o livro aparece na tela
    cy.contains('Livro Encontrado:').should('be.visible');
    cy.contains('Título: Livro E2E').should('be.visible');
    cy.contains('Autor: Autor E2E').should('be.visible');
    cy.contains('ISBN: 123456789').should('be.visible');
    cy.contains('Disponível: Sim').should('be.visible');
  });
});
