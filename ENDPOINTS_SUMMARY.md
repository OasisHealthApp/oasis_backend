# 📡 Resumo Completo dos Endpoints - Oasis API

## Base URL
```
http://localhost:5000/api
```

---

## 🔐 **Autenticação (Auth)**

### 1. Login
```http
POST /api/login
```
**Body:**
```json
{
  "email": "usuario@example.com",
  "senha": "senha123"
}
```
**Response (200):**
```json
{
  "mensagem": "Login realizado com sucesso",
  "token": "jwt_token_aqui",
  "usuario": {
    "id": 1,
    "nome": "João Silva",
    "email": "usuario@example.com"
  }
}
```

### 2. Cadastro
```http
POST /api/signup
```
**Body:**
```json
{
  "nome": "João Silva",
  "email": "usuario@example.com",
  "senha": "senha123",
  "data_nasc": "1990-01-15",
  "idade": 33,
  "sexo": "M"
}
```

### 3. Listar Usuários
```http
GET /api/users
```

---

## 📋 **Hábitos (Habits)**

### 1. Listar Todos os Hábitos
```http
GET /api/habits
```

### 2. Listar Hábitos por Usuário
```http
GET /api/habits/user/{user_id}
```
**Exemplo:** `GET /api/habits/user/1`

### 3. Buscar Hábito por ID
```http
GET /api/habits/{id}
```
**Exemplo:** `GET /api/habits/5`

### 4. Criar Novo Hábito
```http
POST /api/habits
```
**Body:**
```json
{
  "titulo": "Meditação",
  "descricao": "Prática diária de mindfulness",
  "categoria": "cat_bem_estar",
  "frequencia": 1,
  "user_id": 1
}
```
**Response (201):**
```json
{
  "mensagem": "Hábito criado com sucesso",
  "habito": {
    "id": 1,
    "titulo": "Meditação",
    "descricao": "Prática diária de mindfulness",
    "categoria": "cat_bem_estar",
    "frequencia": 1,
    "completado": false,
    "ultimo_completado": null,
    "sequencia_atual": 0,
    "melhor_sequencia": 0,
    "data_criacao": "2025-11-17",
    "user_id": 1
  }
}
```

### 5. Atualizar Hábito
```http
PUT /api/habits/{id}
```
**Body:**
```json
{
  "titulo": "Meditação Matinal",
  "descricao": "Meditar 15 minutos pela manhã",
  "categoria": "cat_bem_estar",
  "frequencia": 1
}
```

### 6. Alternar Status de Completado
```http
POST /api/habits/{id}/toggle
```
**Sem body necessário**

**Response (200):**
```json
{
  "mensagem": "Status atualizado",
  "habito": {
    "id": 1,
    "completado": true,
    "ultimo_completado": "2025-11-17",
    "sequencia_atual": 1,
    ...
  }
}
```

### 7. Excluir Hábito
```http
DELETE /api/habits/{id}
```

---

## 🏷️ **Categorias (Categories)**

### 1. Listar Todas as Categorias
```http
GET /api/categories
```
**Query Params (opcional):**
- `?user_id=1` - Inclui categorias customizadas do usuário

**Response (200):**
```json
[
  {
    "id": "cat_saude",
    "nome": "Saúde",
    "emoji": "🏃",
    "descricao": "Hábitos relacionados à saúde física e mental",
    "cor": "#FF6B6B"
  },
  {
    "id": "cat_produtividade",
    "nome": "Produtividade",
    "emoji": "💼",
    "descricao": "Hábitos para aumentar produtividade e foco",
    "cor": "#4ECDC4"
  }
]
```

### 2. Buscar Categoria por ID
```http
GET /api/categories/{id}
```
**Exemplo:** `GET /api/categories/cat_saude`

### 3. Listar Categorias Customizadas do Usuário
```http
GET /api/categories/user/{user_id}
```
**Exemplo:** `GET /api/categories/user/1`

### 4. Criar Categoria Customizada
```http
POST /api/categories
```
**Body:**
```json
{
  "nome": "Música",
  "emoji": "🎵",
  "descricao": "Praticar instrumentos musicais",
  "cor": "#9B59B6",
  "user_id": 1
}
```

### 5. Atualizar Categoria Customizada
```http
PUT /api/categories/{id}
```
**Body:**
```json
{
  "nome": "Música e Arte",
  "emoji": "🎵",
  "descricao": "Prática musical e artística",
  "cor": "#9B59B6",
  "user_id": 1
}
```

### 6. Excluir Categoria Customizada
```http
DELETE /api/categories/{id}
```
**Body:**
```json
{
  "user_id": 1
}
```

---

## 📖 **Diário (Journal)**

### 1. Listar Todos os Registros
```http
GET /api/journal
```

### 2. Listar Registros por Usuário
```http
GET /api/journal/user/{user_id}
```
**Exemplo:** `GET /api/journal/user/1`

**Response (200):**
```json
[
  {
    "id": 1,
    "conteudo": "Hoje foi um dia muito produtivo...",
    "data": "2025-11-17",
    "user_id": 1,
    "data_criacao": "2025-11-17T14:30:00"
  }
]
```

### 3. Buscar Registro por ID
```http
GET /api/journal/{id}
```

### 4. Buscar Registro por Data
```http
GET /api/journal/user/{user_id}/date/{data}
```
**Exemplo:** `GET /api/journal/user/1/date/2025-11-17`

### 5. Criar Novo Registro
```http
POST /api/journal
```
**Body:**
```json
{
  "conteudo": "Hoje aprendi sobre gestão de tempo...",
  "user_id": 1,
  "data": "2025-11-17"
}
```
**Nota:** Se `data` não for enviada, usa a data atual automaticamente.

**Response (201):**
```json
{
  "mensagem": "Registro criado com sucesso",
  "registro": {
    "id": 1,
    "conteudo": "Hoje aprendi sobre gestão de tempo...",
    "data": "2025-11-17",
    "user_id": 1,
    "data_criacao": "2025-11-17T10:00:00"
  }
}
```

### 6. Atualizar Registro
```http
PUT /api/journal/{id}
```
**Body:**
```json
{
  "conteudo": "Conteúdo atualizado do registro...",
  "user_id": 1
}
```

### 7. Excluir Registro
```http
DELETE /api/journal/{id}
```
**Body:**
```json
{
  "user_id": 1
}
```

---

## 🎨 **Categorias Padrão Disponíveis**

| ID | Nome | Emoji | Cor |
|----|------|-------|-----|
| `cat_saude` | Saúde | 🏃 | #FF6B6B |
| `cat_produtividade` | Produtividade | 💼 | #4ECDC4 |
| `cat_aprendizado` | Aprendizado | 📚 | #95E1D3 |
| `cat_bem_estar` | Bem-estar | 🧘 | #F38181 |
| `cat_social` | Social | 👥 | #AA96DA |
| `cat_financeiro` | Financeiro | 💰 | #FCBAD3 |
| `cat_criatividade` | Criatividade | 🎨 | #FFFFD2 |
| `cat_outros` | Outros | 📌 | #A8DADC |

---

## 📊 **Códigos de Status HTTP**

| Código | Significado |
|--------|-------------|
| 200 | Sucesso (GET, PUT, DELETE) |
| 201 | Criado com sucesso (POST) |
| 400 | Requisição inválida |
| 401 | Não autorizado |
| 404 | Recurso não encontrado |
| 500 | Erro interno do servidor |

---

## 🧪 **Exemplo de Uso com JavaScript (Fetch)**

### Criar Hábito
```javascript
const criarHabito = async () => {
  const response = await fetch('http://localhost:5000/api/habits', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      titulo: 'Exercício',
      descricao: 'Treino de 30 minutos',
      categoria: 'cat_saude',
      frequencia: 1,
      user_id: 1
    })
  });
  
  const data = await response.json();
  console.log(data);
};
```

### Listar Hábitos do Usuário
```javascript
const listarHabitos = async (userId) => {
  const response = await fetch(`http://localhost:5000/api/habits/user/${userId}`);
  const habitos = await response.json();
  console.log(habitos);
};
```

### Alternar Completado
```javascript
const toggleHabito = async (habitId) => {
  const response = await fetch(`http://localhost:5000/api/habits/${habitId}/toggle`, {
    method: 'POST'
  });
  
  const data = await response.json();
  console.log(data);
};
```

---

## ✅ **Checklist de Teste**

- [ ] POST /api/signup - Criar usuário
- [ ] POST /api/login - Fazer login
- [ ] GET /api/categories - Listar categorias
- [ ] POST /api/habits - Criar hábito
- [ ] GET /api/habits/user/1 - Listar hábitos do usuário
- [ ] POST /api/habits/1/toggle - Completar hábito
- [ ] PUT /api/habits/1 - Atualizar hábito
- [ ] DELETE /api/habits/1 - Excluir hábito
- [ ] POST /api/journal - Criar entrada no diário
- [ ] GET /api/journal/user/1 - Listar entradas do usuário
- [ ] PUT /api/journal/1 - Atualizar entrada
- [ ] DELETE /api/journal/1 - Excluir entrada

---

**API pronta para integração! 🚀**
