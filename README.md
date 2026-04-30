# Todolist API com FastAPI

API simples de lista de tarefas desenvolvida com FastAPI, PostgreSQL e Docker.

O objetivo do projeto é estudar a criação de APIs com FastAPI usando uma estrutura organizada em camadas, parecida com o que normalmente usamos em projetos backend profissionais.

## Tecnologias utilizadas

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Docker
- Docker Compose
- uv

## Estrutura do projeto

```txt
todolist-fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── connection.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── task.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── task_repository.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py
│   └── routers/
│       ├── __init__.py
│       └── task_router.py
├── .env
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── uv.lock
└── README.md
```

## Arquitetura utilizada

O projeto segue uma organização em camadas:

```txt
Router -> Service -> Repository -> Model -> Database
```

### Responsabilidade de cada camada

| Camada | Responsabilidade |
|---|---|
| Router | Recebe as requisições HTTP e define os endpoints |
| Service | Contém as regras de negócio |
| Repository | Centraliza as operações com o banco de dados |
| Model | Representa a tabela no banco usando SQLAlchemy |
| Schema | Valida entrada e saída de dados usando Pydantic |
| Database | Configura a conexão com o PostgreSQL |
| Core | Guarda configurações gerais da aplicação |

## Comparação com Laravel

| Laravel | FastAPI |
|---|---|
| routes/api.php | routers |
| Controller | Router |
| Service | Service |
| Eloquent Model | SQLAlchemy Model |
| FormRequest | Pydantic Schema |
| Migration | Alembic |
| Sail | Docker Compose |

## Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd todolist-fastapi
```

### 2. Criar o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=postgresql+psycopg://postgres:postgres@db:5432/todolist
POSTGRES_DB=todolist
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

### 3. Subir os containers

```bash
docker compose up --build
```

A API ficará disponível em:

```txt
http://127.0.0.1:8000
```

A documentação automática ficará disponível em:

```txt
http://127.0.0.1:8000/docs
```

## Endpoints disponíveis

### Health check

```http
GET /
```

Resposta esperada:

```json
{
  "message": "Todolist API rodando"
}
```

### Listar tarefas

```http
GET /tasks
```

### Buscar tarefa por ID

```http
GET /tasks/{task_id}
```

### Criar tarefa

```http
POST /tasks
```

Exemplo de body:

```json
{
  "title": "Estudar FastAPI",
  "description": "Criar uma API de todolist"
}
```

### Atualizar tarefa

```http
PUT /tasks/{task_id}
```

Exemplo de body:

```json
{
  "title": "Estudar FastAPI com Docker",
  "description": "Criar uma API usando PostgreSQL",
  "completed": true
}
```

### Remover tarefa

```http
DELETE /tasks/{task_id}
```

## Model de Task

A tabela `tasks` possui os seguintes campos:

| Campo | Tipo | Descrição |
|---|---|---|
| id | integer | Identificador da tarefa |
| title | string | Título da tarefa |
| description | string | Descrição da tarefa |
| completed | boolean | Indica se a tarefa foi concluída |
| created_at | datetime | Data de criação |
| updated_at | datetime | Data de atualização |

## Comandos úteis

Subir o projeto:

```bash
docker compose up --build
```

Parar os containers:

```bash
docker compose down
```

Parar e apagar o volume do banco:

```bash
docker compose down -v
```

Ver logs:

```bash
docker compose logs -f
```

Acessar o container da API:

```bash
docker exec -it todolist_api bash
```

Acessar o container do banco:

```bash
docker exec -it todolist_db bash
```

## Observação sobre migrations

Atualmente, o projeto cria as tabelas automaticamente usando:

```python
Base.metadata.create_all(bind=engine)
```

Esse recurso é útil para estudo inicial.

Em um projeto profissional, o ideal é usar Alembic para controlar migrations, de forma parecida com as migrations do Laravel.

Fluxo recomendado futuramente:

```bash
uv add alembic
uv run alembic init alembic
uv run alembic revision --autogenerate -m "create tasks table"
uv run alembic upgrade head
```

## Objetivo do projeto

Este projeto foi criado para estudar os principais fundamentos de uma API com FastAPI:

- Criação de rotas
- Organização em camadas
- Validação com Pydantic
- Persistência com SQLAlchemy
- Uso de PostgreSQL
- Ambiente com Docker
- Documentação automática da API