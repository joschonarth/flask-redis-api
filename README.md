# 💾 Python + Flask + Redis

Esta API foi desenvolvida para gerenciar produtos, permitindo a criação e consulta de produtos de forma eficiente e escalável. Utilizando **Python** com o framework **Flask** e o banco de dados **Redis** integrado com **SQLite**, a API otimiza a busca de produtos com um sistema de armazenamento em cache.

## 🛠️ Tecnologias Utilizadas

- 🐍 Python - Linguagem de programação principal utilizada no desenvolvimento da API.
- 🌐 Flask - Framework web utilizado para a criação da API RESTful.
- 💾 Redis - Banco de dados em memória utilizado para armazenamento em cache.
- 🗄️ SQLite3 - Banco de dados relacional utilizado para persistência de produtos.
- 🐳 Docker Compose - Ferramenta para containerização e gerenciamento do ambiente.
- 📏 pylint - Ferramenta de análise estática para garantir a qualidade do código Python.
- 🧪 pytest - Framework de testes utilizado para garantir a confiabilidade do código.

## ⚙️ Funcionalidades

- 📝 Criar Produto - Permite cadastrar um novo produto.
- 🔍 Buscar Produto - Retorna as informações de um produto pelo nome.

## 🚀 Como Executar o Projeto

### 📋 Pré-requisitos

Certifique-se de ter instalado:

- ✅ Python 3+
- ✅ Redis instalado e em execução
- ✅ Docker e Docker Compose (opcional, para containerização)

### 📦 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/joschonarth/flask-redis-api.git
   cd flask-redis-api
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o banco de dados **Redis** utilizando o container Docker com a imagem `redis`:

   ```bash
   docker-compose up -d
   ```

5. Execute a aplicação:

   ```bash
   python run.py
   ```

   A aplicação estará disponível em [http://localhost:5000](http://localhost:5000).

## 🔗 Endpoints

### 📝 Criar Produto

- **Método:** `POST`

- **Rota:** `/products`

- **Corpo da Requisição:**

  ```json
  {
    "name": "new_product",
    "price": 19.99,
    "quantity": 2
  }
  ```

- **Resposta:**

  ```json
  {
    "count": 1,
    "message": "Product registered successfully",
    "type": "PRODUCT"
  }
  ```

### 🔍 Buscar Produto

- **Método:** `GET`
- **Rota:** `/products/:product_name`
- **Path Variables:** `product_name`
- **Resposta:**

  ```json
  {
    "attributes": {
        "name": "new_product",
        "price": 19.99,
        "quantity": 2
    },
    "count": 1,
    "type": "PRODUCT"
  }
  ```

## 💾 Redis e Cache

O **Redis** é um banco de dados em memória utilizado para armazenamento em cache, permitindo respostas rápidas sem acessar diretamente o banco de dados principal. Nesta API:

1. Ao buscar um produto, a API verifica primeiro no **Redis**.
2. Se o produto estiver em cache, a resposta é imediata.
3. Caso contrário, a busca é feita no **SQLite** e o produto é armazenado no **Redis** para futuras consultas.

Isso melhora a performance e reduz o número de acessos ao banco **SQLite**.

## 🧪 Testes

A API inclui testes automatizados utilizando **pytest** para garantir a confiabilidade das funcionalidades.

1. Execute o comando abaixo para rodar todos os testes:

   ```bash
   pytest
   ```

2. Execute os testes com cobertura detalhada:

   ```bash
   pytest -s -v
   ```

## 🤝 Contribuição

Sinta-se à vontade para contribuir! Fique à vontade para abrir issues e pull requests.

## 📞 Contato

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/joschonarth/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:joschonarth@gmail.com)
