# API Quiz AI - Documentação

Esta é a documentação oficial da API do projeto **Quiz AI**. A API foi construída utilizando **Python** com o framework **FastAPI** e utiliza integração com modelos de Inteligência Artificial para gerar perguntas e alternativas sobre temas variados.

## 🚀 Tecnologias

- **Python** e **FastAPI** (Framework Web)
- **Pydantic** (Validação de Dados)
- **PostgreSQL** + **SQLAlchemy** (Banco de Dados e ORM)
- **Uvicorn** (Servidor ASGI)
- **Docker & Docker Compose** (Containerização)

---

## 🛠️ Como Executar o Projeto

1. **Subir os containers do banco de dados:**
   O projeto acompanha um `docker-compose.yaml` com a configuração do PostgreSQL.
   ```bash
   docker-compose up -d
   ```

2. **Instalar as dependências:**
   Na pasta `src`, instale as dependências via pip.
   ```bash
   cd src
   pip install -r requirements.txt
   ```

3. **Configurar variáveis de ambiente:**
   Certifique-se de configurar o seu arquivo `.env` na raiz do projeto ou na pasta `src` com as credenciais do banco de dados e as chaves de API necessárias (ex: `GOOGLE_API_KEY`).

4. **Executar a API localmente:**
   ```bash
   uvicorn main:app --reload
   ```
   A API estará disponível em: `http://localhost:8000`.

---

## 📌 Endpoints da API

A interface interativa do Swagger gerada automaticamente pelo FastAPI (onde você pode testar as rotas) pode ser acessada adicionando `/docs` ou `/redoc` à URL base da aplicação (ex: `http://localhost:8000/docs`).

### 1. Health Check
Verifica se o servidor e a API estão online e funcionando corretamente.

- **URL:** `/`
- **Método HTTP:** `GET`
- **Autenticação:** Não requerida.

**Exemplo de Resposta de Sucesso (200 OK):**
```json
{
  "status": "ok"
}
```

---

### 2. Gerar Questionário (Quiz)
Gera um conjunto de perguntas e alternativas focadas em um tema específico, utilizando um agente de inteligência artificial. As perguntas retornam com as respectivas alternativas corretas e incorretas.

- **URL:** `/question/`
- **Método HTTP:** `POST`
- **Autenticação:** Não requerida (verifique as configurações de CORS se estiver chamando do front-end).

#### 📤 Corpo da Requisição (Request Body)
A requisição espera um JSON com a estrutura `QuestionInput`.

| Campo | Tipo | Descrição | Restrições |
|-------|------|-----------|------------|
| `theme` | `string` | Tema para a criação do questionário. | Obrigatório |
| `question_quantity` | `integer` | Quantidade de questões desejadas no quiz. | Obrigatório, entre 1 e 50 |

**Exemplo de Corpo da Requisição:**
```json
{
  "theme": "História do Brasil",
  "question_quantity": 5
}
```

#### 📥 Resposta (Response Body)
A resposta retorna um objeto JSON `QuestionOutput` contendo a lista das perguntas criadas.

**Exemplo de Resposta de Sucesso (200 OK):**
```json
{
  "questions": [
    {
      "id": 1,
      "title": "Quem foi o responsável pela Proclamação da República no Brasil?",
      "difficulty": "Média",
      "alternatives": [
        {
          "label": "A",
          "text": "Dom Pedro II",
          "is_correct": false
        },
        {
          "label": "B",
          "text": "Marechal Deodoro da Fonseca",
          "is_correct": true
        },
        {
          "label": "C",
          "text": "Getúlio Vargas",
          "is_correct": false
        }
      ]
    }
  ]
}
```

---

## 🗂️ Modelos e Schemas (JSON)

Estes são os detalhes dos modelos estruturais devolvidos e recebidos pelas rotas (`Pydantic Models`):

### `QuestionInput`
| Propriedade | Tipo | Detalhes |
|-------------|------|----------|
| `theme` | `string` | Define o assunto sobre o qual o LLM vai gerar o quiz. |
| `question_quantity` | `integer` | Determina o número de questões retornadas (Min: 1, Máx: 50). |

### `QuestionOutput`
| Propriedade | Tipo | Detalhes |
|-------------|------|----------|
| `questions` | `array de Question` | Lista de objetos do tipo Question. |

### `Question`
| Propriedade | Tipo | Detalhes |
|-------------|------|----------|
| `id` | `integer` | Identificador único numérico da questão gerada. |
| `title` | `string` | O enunciado da pergunta gerada. |
| `difficulty` | `string` | O nível de dificuldade da pergunta. |
| `alternatives`| `array de _Alternative`| Lista de alternativas para a pergunta corrente. |

### `_Alternative` (Alternativa)
| Propriedade | Tipo | Detalhes |
|-------------|------|----------|
| `label` | `string` | Marcador da alternativa (ex: "A", "B", "C"). |
| `text` | `string` | O conteúdo da alternativa. |
| `is_correct` | `boolean` | Indica se a alternativa é a resposta correta (`true`) ou incorreta (`false`). |
