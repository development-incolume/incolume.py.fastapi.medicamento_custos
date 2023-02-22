# ChatGPT

## como construir API com fastapi?
Para construir uma API com o FastAPI, você pode seguir os seguintes passos:

    Instale o FastAPI: Você pode instalar o FastAPI usando o gerenciador de pacotes pip. Abra o terminal e digite o seguinte comando:

pip install fastapi

Crie um arquivo main.py: Crie um arquivo chamado main.py e importe o FastAPI. Você também pode criar uma instância do FastAPI para sua aplicação.

python

from fastapi import FastAPI

app = FastAPI()

Defina rotas: Para criar rotas, você pode usar o decorador @app.route do FastAPI e definir uma função que será executada quando a rota for acessada. A função deve retornar o resultado que será enviado como resposta para o cliente.

python

@app.route("/")
def home():
    return {"message": "Hello, World!"}

Execute a aplicação: Para executar a aplicação, você pode usar o servidor de desenvolvimento do FastAPI. Abra o terminal e digite o seguinte comando:

css

    uvicorn main:app --reload

    Isso iniciará o servidor e você poderá acessar sua API em http://localhost:8000.

    Teste sua API: Você pode usar o navegador ou uma ferramenta de teste de API como o Postman para testar sua API. Acesse a rota http://localhost:8000/ no seu navegador ou envie uma solicitação GET para a mesma rota usando o Postman. Você deve ver a mensagem "Hello, World!" como resposta.

Este é um exemplo básico de como construir uma API com o FastAPI. Há muito mais recursos no FastAPI que você pode usar para criar APIs mais avançadas. Para saber mais, você pode consultar a documentação oficial do FastAPI em https://fastapi.tiangolo.com/.

## e esta mesma api utilizando python poetry?

Claro! Você pode criar um projeto Python usando o Poetry e incluir o FastAPI como uma das dependências do projeto. Aqui estão os passos para criar uma API com o FastAPI usando o Poetry:

    Instale o Poetry: Você pode instalar o Poetry seguindo as instruções em https://python-poetry.org/docs/#installation.

    Crie um novo projeto Poetry: No terminal, navegue para o diretório onde você deseja criar o projeto e execute o seguinte comando para criar um novo projeto Poetry:

    javascript

poetry new nome-do-projeto

Isso criará um novo projeto Poetry com a estrutura de diretórios padrão.

Adicione o FastAPI como uma dependência: No terminal, navegue até o diretório do projeto e execute o seguinte comando para adicionar o FastAPI como uma dependência:

```shell
poetry add fastapi
```

Isso adicionará o FastAPI ao arquivo pyproject.toml do projeto.

Crie um arquivo main.py: Crie um arquivo main.py na raiz do projeto e defina suas rotas e funções como faria normalmente com o FastAPI.

Execute a aplicação: Para executar a aplicação, você pode usar o comando poetry run do Poetry. Abra o terminal, navegue até o diretório do projeto e execute o seguinte comando:

```shell
    poetry run uvicorn main:app --reload

    Isso iniciará o servidor e você poderá acessar sua API em http://localhost:8000.
    Teste sua API: Você pode usar o navegador ou uma ferramenta de teste de API como o Postman para testar sua API. Acesse a rota http://localhost:8000/ no seu navegador ou envie uma solicitação GET para a mesma rota usando o Postman. Você deve ver a mensagem "Hello, World!" como resposta.
```

Esses são os passos básicos para criar uma API com o FastAPI usando o Poetry. Lembre-se de consultar a documentação do Poetry em https://python-poetry.org/docs/ para saber mais sobre o gerenciamento de dependências em projetos Python.

## agora uma interface crud, para controle de preço para medicamento

Certo! Para criar uma interface CRUD para o controle de preço de medicamentos, você pode seguir estes passos:

1. Definir um modelo: Crie uma classe para representar o modelo de dados dos medicamentos. Essa classe pode conter atributos como nome do medicamento, fabricante, dosagem e preço.

```python
from pydantic import BaseModel

class Medicamento(BaseModel):
    nome: str
    fabricante: str
    dosagem: str
    preco: float
```
2. Definir um repositório: Crie um repositório para gerenciar o armazenamento e a recuperação dos dados dos medicamentos. Você pode usar uma lista ou um banco de dados para armazenar os dados. O repositório deve ter métodos para adicionar, atualizar, recuperar e excluir medicamentos.

```python

from typing import List

class MedicamentoRepository:
    def __init__(self):
        self.med_list = []

    def cadastrar_medicamento(self, medicamento: Medicamento):
        self.med_list.append(medicamento)

    def buscar_medicamento(self, nome: str) -> Medicamento:
        for med in self.med_list:
            if med.nome == nome:
                return med
        return None

    def listar_medicamentos(self) -> List[Medicamento]:
        return self.med_list

    def atualizar_medicamento(self, nome: str, medicamento: Medicamento):
        med = self.buscar_medicamento(nome)
        if med:
            index = self.med_list.index(med)
            self.med_list[index] = medicamento

    def excluir_medicamento(self, nome: str):
        med = self.buscar_medicamento(nome)
        if med:
            self.med_list.remove(med)
```
3. Criar as rotas da API: Agora é hora de definir as rotas da API para realizar as operações CRUD nos medicamentos. Você pode usar os métodos do repositório que criou anteriormente para implementar cada rota.

```python

from fastapi import FastAPI
from typing import List

app = FastAPI()
repo = MedicamentoRepository()

@app.post("/medicamentos")
def cadastrar_medicamento(medicamento: Medicamento):
    repo.cadastrar_medicamento(medicamento)
    return {"mensagem": "Medicamento cadastrado com sucesso."}

@app.get("/medicamentos/{nome}")
def buscar_medicamento(nome: str):
    med = repo.buscar_medicamento(nome)
    if med:
        return med
    return {"mensagem": "Medicamento não encontrado."}

@app.get("/medicamentos")
def listar_medicamentos():
    return repo.listar_medicamentos()

@app.put("/medicamentos/{nome}")
def atualizar_medicamento(nome: str, medicamento: Medicamento):
    repo.atualizar_medicamento(nome, medicamento)
    return {"mensagem": "Medicamento atualizado com sucesso."}

@app.delete("/medicamentos/{nome}")
def excluir_medicamento(nome: str):
    repo.excluir_medicamento(nome)
    return {"mensagem": "Medicamento excluído com sucesso."}
```
4. Testar a API: Agora que você criou as rotas da API, pode testá-la usando o Postman ou outra ferramenta de teste de API. Envie solicitações para as rotas da API para criar, atualizar, recuperar e excluir medicamentos. Certifique-se de que os dados estão sendo armazenados corretamente no repositório.


## e como implementar as rotas separadamente?

Para implementar as rotas separadamente, você pode criar um módulo separado para cada rota. Cada módulo terá uma função que define a rota e sua implementação correspondente.

Por exemplo, você pode criar um módulo medicamentos.py com as seguintes funções:

python

from fastapi import APIRouter, HTTPException
from typing import List
from .models import Medicamento
from .repository import MedicamentoRepository

router = APIRouter()
repository = MedicamentoRepository()

@router.post("/medicamentos")
def cadastrar_medicamento(medicamento: Medicamento):
    repository.cadastrar_medicamento(medicamento)
    return {"mensagem": "Medicamento cadastrado com sucesso."}

@router.get("/medicamentos/{nome}")
def buscar_medicamento(nome: str):
    med = repository.buscar_medicamento(nome)
    if med:
        return med
    raise HTTPException(status_code=404, detail="Medicamento não encontrado.")

@router.get("/medicamentos")
def listar_medicamentos():
    return repository.listar_medicamentos()

@router.put("/medicamentos/{nome}")
def atualizar_medicamento(nome: str, medicamento: Medicamento):
    repository.atualizar_medicamento(nome, medicamento)
    return {"mensagem": "Medicamento atualizado com sucesso."}

@router.delete("/medicamentos/{nome}")
def excluir_medicamento(nome: str):
    repository.excluir_medicamento(nome)
    return {"mensagem": "Medicamento excluído com sucesso."}

Em seguida, você pode importar o router do módulo medicamentos.py no arquivo principal da aplicação e adicioná-lo como um roteador na aplicação FastAPI:

python

from fastapi import FastAPI
from .routers import medicamentos

app = FastAPI()

app.include_router(medicamentos.router)

Dessa forma, cada módulo de rota pode ser gerenciado separadamente, tornando a aplicação mais modular e fácil de manter.

## faça para mim o diagrama desta estrutra

Claro, aqui está um possível diagrama para a estrutura que descrevemos anteriormente:

```python

+-------------------+      +------------------------+
|    main.py        |      |   routers/medicamentos  |
+-------------------+      +------------------------+
|   import FastAPI  |      |   import APIRouter      |
|   import MedicamentoRepository |   import Medicamento |
|   import medicamentos |   |   import HTTPException |
|                   |      |   import repository     |
|                   |      |                        |
|   app = FastAPI() |      |   router = APIRouter()  |
|   app.include_router(medicamentos.router) |        |
|                   |      |                        |
+-------------------+      +------------------------+
                            |   @router.post("/medicamentos") |
                            |   def cadastrar_medicamento(medicamento: Medicamento): |
                            |       repository.cadastrar_medicamento(medicamento) |
                            |       return {"mensagem": "Medicamento cadastrado com sucesso."} |
                            |   ... |
```
Este diagrama mostra a relação entre o arquivo principal main.py e o módulo routers/medicamentos.py. O arquivo principal main.py importa o FastAPI e o MedicamentoRepository, bem como o módulo routers/medicamentos.py. Dentro do módulo routers/medicamentos.py, importamos o APIRouter, Medicamento, HTTPException e MedicamentoRepository. Cada função do APIRouter corresponde a uma rota específica, como cadastrar_medicamento(), buscar_medicamento(), listar_medicamentos(), atualizar_medicamento() e excluir_medicamento(). Estas funções utilizam a classe MedicamentoRepository para executar as operações CRUD no banco de dados.

Espero que este diagrama ajude a entender melhor a estrutura da aplicação!


## e como faço uma conexão deste programa um com um SGBD?

Para fazer a conexão do seu programa com um SGBD, você pode usar uma biblioteca de acesso a banco de dados, como o SQLAlchemy, que é compatível com diversos SGBDs, como SQLite, MySQL, PostgreSQL, Oracle, entre outros.

Primeiro, é preciso instalar a biblioteca SQLAlchemy e o driver correspondente ao seu SGBD. Por exemplo, se você quiser usar o PostgreSQL como seu SGBD, pode instalar o driver psycopg2 junto com o SQLAlchemy, executando o seguinte comando no seu terminal:

php

pip install sqlalchemy psycopg2-binary

Em seguida, você pode criar uma classe para gerenciar a conexão com o banco de dados e executar as operações CRUD. Por exemplo:

python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Medicamento

class MedicamentoRepository:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def cadastrar_medicamento(self, medicamento: Medicamento):
        self.session.add(medicamento)
        self.session.commit()

    def buscar_medicamento(self, nome: str):
        return self.session.query(Medicamento).filter_by(nome=nome).first()

    def listar_medicamentos(self):
        return self.session.query(Medicamento).all()

    def atualizar_medicamento(self, nome: str, medicamento: Medicamento):
        med = self.buscar_medicamento(nome)
        if med:
            med.nome = medicamento.nome
            med.preco = medicamento.preco
            self.session.commit()

    def excluir_medicamento(self, nome: str):
        med = self.buscar_medicamento(nome)
        if med:
            self.session.delete(med)
            self.session.commit()

Esta classe utiliza o SQLAlchemy para criar uma conexão com o banco de dados especificado na URL passada como parâmetro no construtor. Em seguida, as funções CRUD são implementadas utilizando a sessão criada.

Para usar essa classe, você pode instanciá-la no seu arquivo principal main.py passando a URL de conexão do seu SGBD. Por exemplo, se você estiver usando o PostgreSQL, pode criar uma URL de conexão como:

bash

postgresql://user:password@localhost/db_name

E então, instanciar a classe MedicamentoRepository:

python

from fastapi import FastAPI
from .routers import medicamentos
from .repository import MedicamentoRepository

app = FastAPI()

db_url = "postgresql://user:password@localhost/db_name"
repository = MedicamentoRepository(db_url)

app.include_router(medicamentos.router)

Dessa forma, a sua aplicação estará conectada ao seu SGBD e poderá realizar operações CRUD no banco de dados especificado.


## e utlizando o modelo de dados do pydantic

Para utilizar o modelo de dados do Pydantic em conjunto com o SQLAlchemy, você pode definir suas classes do modelo utilizando o Pydantic e, em seguida, criar uma classe do modelo de dados do SQLAlchemy que herda do modelo do Pydantic.

Por exemplo, para a classe Medicamento, você pode definir o modelo do Pydantic da seguinte forma:

python

from pydantic import BaseModel

class MedicamentoBase(BaseModel):
    nome: str
    preco: float

Em seguida, você pode definir um modelo do Pydantic que herda do MedicamentoBase para ser utilizado como entrada em suas rotas:

python

class MedicamentoCreate(MedicamentoBase):
    pass

E um modelo do Pydantic que herda do MedicamentoBase para ser utilizado como saída em suas rotas:

python

class Medicamento(MedicamentoBase):
    id: int

    class Config:
        orm_mode = True

Agora, você pode utilizar o modelo Medicamento como base para a criação da tabela no banco de dados, utilizando o SQLAlchemy:

python

from sqlalchemy import Column, Integer, String, Float
from .database import Base

class MedicamentoModel(Base):
    __tablename__ = "medicamentos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    preco = Column(Float)

Note que a classe MedicamentoModel herda da classe Base importada do módulo database. Esta classe Base é uma classe do SQLAlchemy que contém a definição do objeto metadata utilizado para definir a estrutura do banco de dados.

Para fazer a conexão com o banco de dados e executar as operações CRUD, você pode utilizar uma classe de repositório, como a que eu mostrei na resposta anterior, e atualizá-la para fazer uso do modelo de dados do Pydantic e do SQLAlchemy:

python

from sqlalchemy.orm import Session
from .models import Medicamento, MedicamentoModel

class MedicamentoRepository:
    def __init__(self, db_session: Session):
        self.session = db_session

    def cadastrar_medicamento(self, medicamento: Medicamento):
        medicamento_model = MedicamentoModel(**medicamento.dict())
        self.session.add(medicamento_model)
        self.session.commit()
        self.session.refresh(medicamento_model)
        return medicamento_model

    def buscar_medicamento(self, nome: str):
        medicamento_model = self.session.query(MedicamentoModel).filter_by(nome=nome).first()
        return Medicamento.from_orm(medicamento_model) if medicamento_model else None

    def listar_medicamentos(self):
        medicamento_models = self.session.query(MedicamentoModel).all()
        return [Medicamento.from_orm(medicamento_model) for medicamento_model in medicamento_models]

    def atualizar_medicamento(self, nome: str, medicamento: Medicamento):
        medicamento_model = self.session.query(MedicamentoModel).filter_by(nome=nome).first()
        if medicamento_model:
            medicamento_model.nome = medicamento.nome
            medicamento_model.preco = medicamento.preco
            self.session.commit()
            self.session.refresh(medicamento_model)
            return medicamento_model
        else:
            return None

    def excluir_medicamento(self, nome: str):
        medicamento_model = self.session.query(MedicamentoModel).filter_by(nome=nome).first()
        if medicamento


## e se eu quiser utilizar um docker para container?

Você pode utilizar o Docker para criar um container para a sua aplicação e para o seu banco de dados. O uso de containers pode facilitar a instalação e a execução da sua aplicação em diferentes ambientes.

Para utilizar o Docker, você precisará criar um arquivo chamado Dockerfile na raiz do seu projeto. Este arquivo será utilizado para definir a imagem do seu container e as etapas necessárias para construí-lo.

Um exemplo de Dockerfile para a sua aplicação pode ser o seguinte:

dockerfile

# Definir a imagem base
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Copiar o arquivo requirements.txt para o container
COPY ./app/requirements.txt /app/requirements.txt

# Instalar as dependências da aplicação
RUN pip install -r /app/requirements.txt

# Copiar o diretório app para o container
COPY ./app /app

# Definir o comando para iniciar o servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

Este Dockerfile define a imagem base como tiangolo/uvicorn-gunicorn-fastapi:python3.9, que é uma imagem do Docker Hub que já inclui o Uvicorn, o Gunicorn e o FastAPI. Em seguida, ele copia o arquivo requirements.txt para o container e instala as dependências da aplicação. Por fim, ele copia todo o diretório app para o container e define o comando para iniciar o servidor.

Para criar a imagem do seu container, basta executar o comando docker build na raiz do seu projeto, passando um nome e uma tag para a imagem:

docker build -t meu-app:1.0 .

Isso criará uma imagem com o nome meu-app e a tag 1.0, utilizando o Dockerfile na raiz do seu projeto.

Para executar a aplicação em um container, você precisará criar um arquivo docker-compose.yml, que é utilizado para definir a configuração dos seus containers. Um exemplo de docker-compose.yml para a sua aplicação pode ser o seguinte:

yaml

version: "3.9"

services:
  db:
    image: postgres:13
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: medicamentos
    ports:
      - "5432:5432"
    volumes:
      - db-data:/var/lib/postgresql/data

  app:
    build: .
    ports:
      - "80:80"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/medicamentos

volumes:
  db-data:

Este arquivo define dois serviços: um para o banco de dados PostgreSQL e outro para a sua aplicação. O serviço do banco de dados utiliza a imagem oficial do PostgreSQL no Docker Hub e define as variáveis de ambiente necessárias para configurar o usuário, a senha e o nome do banco de dados.

O serviço da aplicação utiliza a imagem criada a partir do Dockerfile e define a porta em que a aplicação será executada. Ele também define a dependência em relação ao serviço do banco de dados e define a variável de ambiente DATABASE_URL, que é utilizada pela aplicação para se conectar ao banco de dados.

Para iniciar os containers, basta executar o comando `docker-compose


## tem como acrescentar um cache com redis?

Sim, é possível implementar um cache utilizando o Redis para melhorar a performance da sua API. O Redis é um banco de dados em memória que pode ser utilizado para armazenar dados em cache, tornando o acesso aos dados mais rápido.

Para utilizar o Redis como cache na sua aplicação, você pode utilizar a biblioteca aioredis. Para instalá-la, basta adicionar a seguinte linha no seu arquivo requirements.txt:

aioredis

Em seguida, você pode criar uma conexão com o Redis na inicialização da sua aplicação. Para isso, você pode criar uma função create_redis_pool que retorna uma conexão com o Redis:

python

import aioredis

async def create_redis_pool():
    redis_pool = await aioredis.create_redis_pool('redis://redis:6379')
    return redis_pool

Esta função utiliza a biblioteca aioredis para criar uma conexão com o Redis na URL redis://redis:6379. Esta URL assume que o Redis está sendo executado em um container com o nome redis. Se você estiver executando o Redis em um servidor separado, deverá ajustar a URL para apontar para o endereço correto.

Você pode utilizar esta função para criar um pool de conexões com o Redis e armazená-lo em uma variável global da sua aplicação:

python

from fastapi import FastAPI
from app.api import medicamentos
import aioredis

app = FastAPI()

redis_pool = None

@app.on_event("startup")
async def startup_event():
    global redis_pool
    redis_pool = await create_redis_pool()

@app.on_event("shutdown")
async def shutdown_event():
    global redis_pool
    redis_pool.close()
    await redis_pool.wait_closed()

app.include_router(medicamentos.router)

Este código cria uma variável global redis_pool que será utilizada para armazenar as conexões com o Redis. Ele também utiliza os eventos startup e shutdown do FastAPI para criar e fechar o pool de conexões com o Redis.

Com a conexão com o Redis criada, você pode utilizar a função get e set para armazenar e recuperar dados em cache. Por exemplo, você pode criar uma função get_medicamentos que verifica se os dados já estão em cache e, se não estiverem, busca os dados no banco de dados e os armazena em cache:

python

import json

async def get_medicamentos(db, redis_pool):
    medicamentos_cache = await redis_pool.get('medicamentos_cache')
    if medicamentos_cache is not None:
        return json.loads(medicamentos_cache)
    else:
        medicamentos = await db.get_medicamentos()
        medicamentos_cache = json.dumps(medicamentos)
        await redis_pool.set('medicamentos_cache', medicamentos_cache, expire=3600)
        return medicamentos

Esta função verifica se existe um valor no cache com a chave medicamentos_cache. Se existir, ela retorna os dados em cache. Se não existir, ela busca os dados no banco de dados e os armazena em cache utilizando a função set do Redis. O parâmetro expire=3600 define que o valor armazenado em cache expirará após uma hora (3600 segundos).

Com esta implementação, a função get_medicamentos será utilizada para buscar os dados dos medicamentos. A primeira vez que a função for chamada, ela buscará os dados no banco de dados e os armazenará em cache. Nas chamadas

## lembre-se estou utilizando poetry

Sim, para utilizar o Redis com Poetry, você pode seguir os seguintes passos:

    Adicione a dependência do aioredis no seu arquivo pyproject.toml:

csharp

[tool.poetry.dependencies]
aioredis = "^2.0.0"

    Execute o comando poetry install para instalar a nova dependência.

    Crie um arquivo redis.py na raiz do seu projeto e adicione o seguinte código:

python

import aioredis

async def create_redis_pool():
    redis_pool = await aioredis.create_redis_pool('redis://redis:6379')
    return redis_pool

    No arquivo main.py, importe a função create_redis_pool do arquivo redis.py e utilize-a para criar um pool de conexões com o Redis:

python

from fastapi import FastAPI
from app.api import medicamentos
from redis import create_redis_pool

app = FastAPI()

redis_pool = None

@app.on_event("startup")
async def startup_event():
    global redis_pool
    redis_pool = await create_redis_pool()

@app.on_event("shutdown")
async def shutdown_event():
    global redis_pool
    redis_pool.close()
    await redis_pool.wait_closed()

app.include_router(medicamentos.router)

Com esses passos, você pode utilizar o Redis como cache na sua aplicação FastAPI utilizando o Poetry.

## e como ficará toda esta configuração?
4 / 4

Segue abaixo um exemplo de como ficará toda essa configuração utilizando o Redis como cache na aplicação FastAPI com Poetry:

pyproject.toml

makefile

[tool.poetry]
name = "fastapi-redis"
version = "0.1.0"
description = ""
authors = ["Seu Nome <seu.email@exemplo.com>"]

[tool.poetry.dependencies]
python = "^3.10.0"
fastapi = "^0.68.1"
uvicorn = "^0.15.0"
aioredis = "^2.0.0"

[tool.poetry.dev-dependencies]
pytest = "^6.2.4"
pytest-asyncio = "^0.15.1"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

app/api/medicamentos.py

python

from fastapi import APIRouter, Depends, HTTPException
from redis import Redis
from typing import List
from app.models import Medicamento, MedicamentoCreate, MedicamentoUpdate
from app.database import get_medicamentos_repository, MedicamentosRepository

router = APIRouter()

@router.get("/medicamentos", response_model=List[Medicamento])
async def read_medicamentos(skip: int = 0, limit: int = 100, medicamentos_repo: MedicamentosRepository = Depends(get_medicamentos_repository), redis: Redis = Depends(create_redis_pool)):
    medicamentos = await medicamentos_repo.get_medicamentos(skip=skip, limit=limit)

    # Verifica se o cache existe
    cached_medicamentos = await redis.get(f"medicamentos:{skip}:{limit}")
    if cached_medicamentos:
        return cached_medicamentos

    # Se o cache não existe, salva o resultado da consulta no cache
    medicamentos_json = medicamentos.json()
    await redis.set(f"medicamentos:{skip}:{limit}", medicamentos_json)
    return medicamentos

@router.post("/medicamentos", response_model=Medicamento)
async def create_medicamento(medicamento: MedicamentoCreate, medicamentos_repo: MedicamentosRepository = Depends(get_medicamentos_repository)):
    return await medicamentos_repo.create_medicamento(medicamento)

@router.put("/medicamentos/{id}", response_model=Medicamento)
async def update_medicamento(id: int, medicamento: MedicamentoUpdate, medicamentos_repo: MedicamentosRepository = Depends(get_medicamentos_repository)):
    db_medicamento = await medicamentos_repo.get_medicamento_by_id(id)
    if not db_medicamento:
        raise HTTPException(status_code=404, detail="Medicamento não encontrado")

    return await medicamentos_repo.update_medicamento(id, medicamento)

@router.delete("/medicamentos/{id}")
async def delete_medicamento(id: int, medicamentos_repo: MedicamentosRepository = Depends(get_medicamentos_repository)):
    db_medicamento = await medicamentos_repo.get_medicamento_by_id(id)
    if not db_medicamento:
        raise HTTPException(status_code=404, detail="Medicamento não encontrado")

    await medicamentos_repo.delete_medicamento(id)

app/database.py

python

from motor.motor_asyncio import AsyncIOMotorClient
from app.repositories import MotorMedicamentosRepository, MedicamentosRepository

async def connect_to_mongo():
    client = AsyncIOMotorClient("mongodb://mongo:27017")
    return client

async def close_mongo_connection(client):
    client.close()

def get_medicamentos_repository():
    return MotorMedicamentosRepository()

class Motor

## a resposta parece incompleta. Não contem as informações de respostas anteriores...

Peço desculpas pelo erro. Realmente faltou a parte da resposta anterior. Segue a resposta completa:

Segue abaixo um exemplo de como ficará toda essa configuração utilizando o Redis como cache na aplicação FastAPI com Poetry:

pyproject.toml

makefile

[tool.poetry]
name = "fastapi-redis"
version = "0.1.0"
description = ""
authors = ["Seu Nome <seu.email@exemplo.com>"]

[tool.poetry.dependencies]
python = "^3.10.0"
fastapi = "^0.68.1"
uvicorn = "^0.15.0"
aioredis = "^2.0.0"

[tool.poetry.dev-dependencies]
pytest = "^6.2.4"
pytest-asyncio = "^0.15.1"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

app/api/medicamentos.py

python

from fastapi import APIRouter, Depends, HTTPException
from redis import Redis
from typing import List
from app.models import Medicamento, MedicamentoCreate, MedicamentoUpdate
from app.database import get_medicamentos_repository, MedicamentosRepository

router = APIRouter()

@router.get("/medicamentos", response_model=List[Medicamento])
async def read_medicamentos(skip: int = 0, limit: int = 100, medicamentos_repo: MedicamentosRepository = Depends(get_medicamentos_repository), redis: Redis = Depends(create_redis_pool)):
    medicamentos = await medicamentos_repo.get_medicamentos(skip=skip, limit=limit)

    # Verifica se o cache existe
    cached_medicamentos = await redis.get(f"medicamentos:{skip}:{limit}")
    if cached_medicamentos:
        return cached_medicamentos

    # Se o cache não existe, salva o resultado da consulta no cache
    medicamentos_json = medicamentos.json()
    await redis.set(f"medicamentos:{skip}:{limit}", medicamentos_json)
    return medicamentos

@router.post("/medicamentos", response_model=Medicamento)
async def create_medicamento(medicamento: MedicamentoCreate, medicamentos_repo: MedicamentosRepository = Depends(get_medicamentos_repository)):
    return await medicamentos_repo.create_medicamento(medicamento)

@router.put("/medicamentos/{id}", response_model=Medicamento)
async def update_medicamento(id: int, medicamento: MedicamentoUpdate, medicamentos_repo: MedicamentosRepository = Depends(get_medicamentos_repository)):
    db_medicamento = await medicamentos_repo.get_medicamento_by_id(id)
    if not db_medicamento:
        raise HTTPException(status_code=404, detail="Medicamento não encontrado")

    return await medicamentos_repo.update_medicamento(id, medicamento)

@router.delete("/medicamentos/{id}")
async def delete_medicamento(id: int, medicamentos_repo: MedicamentosRepository = Depends(get_medicamentos_repository)):
    db_medicamento = await medicamentos_repo.get_medicamento_by_id(id)
    if not db_medicamento:
        raise HTTPException(status_code=404, detail="Medicamento não encontrado")

    await medicamentos_repo.delete_medicamento(id)

app/database.py

python

from motor.motor_asyncio import AsyncIOMotorClient
from app.repositories import MotorMedicamentosRepository, MedicamentosRepository

async def connect_to_mongo():
    client = AsyncIOMotorClient("mongodb://mongo:27017")
    return client

async def close_m

Ricardo Brito
e como ficará toda esta configuração docker + FastAPI + SGBD + cache redis?

Segue abaixo um exemplo de como ficará toda essa configuração utilizando Docker Compose para executar a aplicação FastAPI com Redis como cache e MongoDB como banco de dados:

Dockerfile

dockerfile

FROM python:3.10.0

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY app /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

docker-compose.yml

yaml

version: "3.9"

services:
  app:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - mongo
      - redis
    environment:
      - MONGODB_HOST=mongo
      - MONGODB_PORT=27017
      - REDIS_HOST=redis
      - REDIS_PORT=6379
  mongo:
    image: mongo:5.0.5
    environment:
      - MONGO_INITDB_DATABASE=medicamentos
    volumes:
      - ./mongo-init.js:/docker-entrypoint-initdb.d/mongo-init.js:ro
  redis:
    image: redis:6.2.6
    command: redis-server --requirepass yourpassword
    environment:
      - REDIS_PASSWORD=yourpassword
    ports:
      - "6379:6379"

mongo-init.js

js

db.createUser({
  user: "user",
  pwd: "password",
  roles: [{ role: "readWrite", db: "medicamentos" }],
});

app/main.py

python

from fastapi import FastAPI
from app.api import medicamentos
from app.database import connect_to_mongo, close_mongo_connection
from redis import Redis
from aioredis import create_redis_pool

app = FastAPI()

@app.on_event("startup")
async def startup():
    app.mongo_client = await connect_to_mongo()
    app.redis_pool = await create_redis_pool("redis://yourpassword@redis:6379/0")

@app.on_event("shutdown")
async def shutdown():
    app.mongo_client.close()
    await close_mongo_connection()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(medicamentos.router)

def create_redis_pool():
    async def _create_redis_pool():
        redis = Redis(host="redis", password="yourpassword", port=6379, db=0)
        await redis.wait_until_ready()
        return redis
    return _create_redis_pool

app/api/medicamentos.py

python

from fastapi import APIRouter, Depends, HTTPException
from redis import Redis
from typing import List
from app.models import Medicamento, MedicamentoCreate, MedicamentoUpdate
from app.database import get_medicamentos_repository, MedicamentosRepository

router = APIRouter()

@router.get("/medicamentos", response_model=List[Medicamento])
async def read_medicamentos(skip: int = 0, limit: int = 100, medicamentos_repo: MedicamentosRepository = Depends(get_medicamentos_repository), redis: Redis = Depends(create_redis_pool())):
    medicamentos = await medicamentos_repo.get_medicamentos(skip=skip, limit=limit)

    # Verifica se o cache existe
    cached_medicamentos = await redis.get(f"medicamentos:{skip}:{limit}")
    if cached_medicamentos:
        return cached_medicamentos

    # Se o cache não existe, salva o resultado

Ricardo Brito
e como ficará toda esta configuração docker + FastAPI + SGBDR + cache redis?

Segue abaixo um exemplo de como ficará toda essa configuração utilizando Docker Compose para executar a aplicação FastAPI com Redis como cache e PostgreSQL como SGBDR:

Dockerfile

dockerfile

FROM python:3.10.0

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY app /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

docker-compose.yml

yaml

version: "3.9"

services:
  app:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - postgres
      - redis
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=medicamentos
      - POSTGRES_HOST=postgres
      - POSTGRES_PORT=5432
      - REDIS_HOST=redis
      - REDIS_PORT=6379
  postgres:
    image: postgres:14.1
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=medicamentos
    volumes:
      - ./postgres-init.sql:/docker-entrypoint-initdb.d/postgres-init.sql:ro
  redis:
    image: redis:6.2.6
    command: redis-server --requirepass yourpassword
    environment:
      - REDIS_PASSWORD=yourpassword
    ports:
      - "6379:6379"

postgres-init.sql

sql

CREATE TABLE medicamentos (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  descricao TEXT,
  preco NUMERIC(8, 2)
);

app/main.py

python

from fastapi import FastAPI
from app.api import medicamentos
from app.database import connect_to_postgres, close_postgres_connection
from redis import Redis
from aioredis import create_redis_pool

app = FastAPI()

@app.on_event("startup")
async def startup():
    app.postgres_client = await connect_to_postgres()
    app.redis_pool = await create_redis_pool("redis://yourpassword@redis:6379/0")

@app.on_event("shutdown")
async def shutdown():
    await close_postgres_connection()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(medicamentos.router)

def create_redis_pool():
    async def _create_redis_pool():
        redis = Redis(host="redis", password="yourpassword", port=6379, db=0)
        await redis.wait_until_ready()
        return redis
    return _create_redis_pool

app/api/medicamentos.py

python

from fastapi import APIRouter, Depends, HTTPException
from redis import Redis
from typing import List
from app.models import Medicamento, MedicamentoCreate, MedicamentoUpdate
from app.database import get_medicamentos_repository, MedicamentosRepository

router = APIRouter()

@router.get("/medicamentos", response_model=List[Medicamento])
async def read_medicamentos(skip: int = 0, limit: int = 100, medicamentos_repo: MedicamentosRepository = Depends(get_medicamentos_repository), redis: Redis = Depends(create_redis_pool())):
    medicamentos = await medicamentos_repo.get_medicamentos(skip=skip, limit=limit)

    # Verifica se o cache existe
    cached_medicamentos = await redis.get(f"medicamentos:{

Ricardo Brito
e como ficará toda esta configuração docker + FastAPI + pydantic + SGBD + cache redis?

Segue abaixo um exemplo de como ficará toda essa configuração utilizando Docker Compose para executar a aplicação FastAPI com Redis como cache, PostgreSQL como SGBD e Pydantic para validação de dados:

Dockerfile

dockerfile

FROM python:3.10.0

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY app /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

docker-compose.yml

yaml

version: "3.9"

services:
  app:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - postgres
      - redis
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=medicamentos
      - POSTGRES_HOST=postgres
      - POSTGRES_PORT=5432
      - REDIS_HOST=redis
      - REDIS_PORT=6379
  postgres:
    image: postgres:14.1
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=medicamentos
    volumes:
      - ./postgres-init.sql:/docker-entrypoint-initdb.d/postgres-init.sql:ro
  redis:
    image: redis:6.2.6
    command: redis-server --requirepass yourpassword
    environment:
      - REDIS_PASSWORD=yourpassword
    ports:
      - "6379:6379"

postgres-init.sql

sql

CREATE TABLE medicamentos (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  descricao TEXT,
  preco NUMERIC(8, 2)
);

app/main.py

python

from fastapi import FastAPI
from app.api import medicamentos
from app.database import connect_to_postgres, close_postgres_connection
from redis import Redis
from aioredis import create_redis_pool
from pydantic import BaseModel

app = FastAPI()

class MedicamentoBase(BaseModel):
    nome: str
    descricao: str = None
    preco: float

class MedicamentoCreate(MedicamentoBase):
    pass

class MedicamentoUpdate(MedicamentoBase):
    id: int

class Medicamento(MedicamentoBase):
    id: int

@app.on_event("startup")
async def startup():
    app.postgres_client = await connect_to_postgres()
    app.redis_pool = await create_redis_pool("redis://yourpassword@redis:6379/0")

@app.on_event("shutdown")
async def shutdown():
    await close_postgres_connection()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(medicamentos.router)

def create_redis_pool():
    async def _create_redis_pool():
        redis = Redis(host="redis", password="yourpassword", port=6379, db=0)
        await redis.wait_until_ready()
        return redis
    return _create_redis_pool

app/api/medicamentos.py

python

from fastapi import APIRouter, Depends, HTTPException
from redis import Redis
from typing import List
from app.models import Medicamento, MedicamentoCreate, MedicamentoUpdate
from app.database import get_medicamentos_repository, MedicamentosRepository

router = APIRouter()

@router.get("/medicamentos", response_model=List[Medicamento])
async def read_medicamentos(skip: int =
