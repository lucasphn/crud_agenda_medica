# crud-agenda-medica

A estrutura do projeto seguirá o Model-View-Controller (MVC)

![Imagem Projeto](assets/esquema_do_projeto.png)

A adaptação será em nossa estrutura de CRUD, onde teremos um arquivo que armazenará as requisições e respostas, e outro que transformará essas funções em ações GET (Select), POST (Insert), DELETE (Delete), PUT (Update). 

Para isso, usamos decoradores da biblioteca FAST API, além de bibliotecas como Pydantic para qualificar nossos dados e SQLAlchemy para ler objetos em Python e transmiti-los aos nossos dados reais.

## Instruções para rodar o código

**Para rodar a aplicação em seu computador:**

1. Faça o Download do Docker;
2. Clone este repositório para sua máquina;
3. Salve-a em um local de sua escolha;
4. Em seu prompt de comando, navegue até a pasta do repositório raiz do projeto;
5. Ainda no prompt de comando, execute a seguinte linha de código: `docker compose up`

### Comando `docker-compose up`:

Quando você executa `docker-compose up`, o Docker Compose lerá o arquivo `docker-compose.yml`, criará os serviços conforme as definições especificadas e os iniciará. Isso significa que os contêineres para o banco de dados PostgreSQL, o backend e o frontend serão criados e conectados à rede `mynetwork`. O banco de dados será configurado com os detalhes fornecidos (nome do banco de dados, usuário e senha), e as imagens para os serviços de backend e frontend serão construídas a partir dos Dockerfiles fornecidos. Uma vez iniciados, você poderá acessar o backend através de `http://localhost:8000` e o frontend através de `http://localhost:8501`. Os dados do banco de dados serão persistidos no volume `postgres_data`.

Pronto! Agora você pode abrir a porta liberada para aplicação em seu navegador.

### Uso
Frontend: Acesse o endereço http://localhost:8501

### Documentação
Backend: Acesse o endereço http://localhost:8000/docs

## Nossa estrutura de pastas e arquivos

```bash
├── README.md # arquivo com a documentação do projeto
├── backend # pasta do backend (FastAPI, SQLAlchemy, Uvicorn, Pydantic)
├── frontend # pasta do frontend (Streamlit, Requests, Pandas)
├── docker-compose.yml # arquivo de configuração do docker-compose (backend, frontend, postgres)
```
