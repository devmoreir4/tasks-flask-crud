# Task Manager API

Este projeto implementa uma API simples para criar, ler, atualizar e deletar tarefas (CRUD). A aplicação foi desenvolvida com o framework Flask, e conta com um conjunto de testes automatizados para garantir a funcionalidade correta dos endpoints.

## Funcionalidades
- Criar Tarefa: Adiciona uma nova tarefa com título e, opcionalmente, descrição.
- Listar Tarefas: Retorna todas as tarefas cadastradas junto com o total de tarefas.
- Obter Tarefa: Busca os detalhes de uma tarefa específica através do seu ID.
- Atualizar Tarefa: Modifica os dados de uma tarefa existente.
- Deletar Tarefa: Remove uma tarefa da lista.

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/devmoreir4/tasks-flask-crud.git
   ```

2. **Entre no diretório do projeto:**

   ```bash
   cd tasks-flask-crud
   ```

3. **Crie e ative um ambiente virtual (opcional):**

   - No Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - No Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

4. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

## Como Executar a Aplicação

- **Inicie o Servidor:**

   ```bash
   python app.py
   ```
A API ficará disponível em: http://127.0.0.1:5000


## Endpoints

1. **Criar Tarefa**
    - URL: /tasks
    - Método: POST
    - Payload Exemplo:
   ```json
    {
        "title": "Título da Tarefa",
        "description": "Descrição da tarefa"
    }
   ```
   - Resposta:
   ```json
    {
        "message": "Task created successfully",
        "id": 1
    }
   ```

2. **Listar Tarefas**
    - URL: /tasks
    - Método: GET
    - Resposta:
    ```json
    {
        "tasks": [
            {
            "id": 1,
            "title": "Título da Tarefa",
            "description": "Descrição da tarefa",
            "completed": false
            }
        ],
        "total_tasks": 1
    }
   ```

3. **Obter Tarefa**
    - URL: /tasks/<int:id>
    - Método: GET
    - Resposta (caso exista):
   ```json
    {
        "id": 1,
        "title": "Título da Tarefa",
        "description": "Descrição da tarefa",
        "completed": false
    }
   ```
    - Resposta (caso não exista):
    ```json
    {
        "message": "Task not found"
    }
    ```


4. **Atualizar Tarefa**
    - URL: /tasks/<int:id>
    - Método: PUT
    - Payload Exemplo:
   ```json
    {
        "title": "Novo título",
        "description": "Nova descrição",
        "completed": true
    }
   ```
    - Resposta:
    ```json
    {
        "message": "Task updated successfully"
    }
    ```

2. **Deletar Tarefa**
    - URL: /tasks/<int:id>
    - Método: DELETE
    - Resposta:
    ```json
    {
        "message": "Task deleted successfully"
    }
   ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir *issues* ou enviar *pull requests* para contribuir com o projeto.


## Licença

Este projeto está licenciado sob a licença MIT.
