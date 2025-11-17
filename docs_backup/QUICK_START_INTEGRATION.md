# 🚀 Quick Start - Testando a Integração

## 1️⃣ Inicie o Backend

```bash
cd "/home/abraao/Área de trabalho/oasis_backend"
source OasisVenv/bin/activate
python app.py
```

Servidor rodando em: **http://localhost:5000**

---

## 2️⃣ Teste os Endpoints

### Verificar se API está online
```bash
curl http://localhost:5000
```

### Listar Categorias Padrão
```bash
curl http://localhost:5000/api/categories
```

### Criar um Usuário
```bash
curl -X POST http://localhost:5000/api/signup \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João Silva",
    "email": "joao@oasis.com",
    "senha": "senha123"
  }'
```

### Fazer Login
```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "joao@oasis.com",
    "senha": "senha123"
  }'
```

### Criar um Hábito
```bash
curl -X POST http://localhost:5000/api/habits \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Meditação",
    "descricao": "Prática diária de mindfulness",
    "categoria": "cat_bem_estar",
    "frequencia": 1,
    "user_id": 1
  }'
```

### Listar Hábitos do Usuário
```bash
curl http://localhost:5000/api/habits/user/1
```

### Completar um Hábito
```bash
curl -X POST http://localhost:5000/api/habits/1/toggle
```

### Criar Entrada no Diário
```bash
curl -X POST http://localhost:5000/api/journal \
  -H "Content-Type: application/json" \
  -d '{
    "conteudo": "Hoje foi um dia muito produtivo. Consegui completar todos os meus hábitos!",
    "user_id": 1
  }'
```

### Listar Entradas do Diário
```bash
curl http://localhost:5000/api/journal/user/1
```

---

## 3️⃣ Abra o Front-End

### Opção 1: Live Server (VS Code)
1. Abra `/home/abraao/Downloads/OASIS_FRONT_END` no VS Code
2. Clique com botão direito em `index.html`
3. Selecione "Open with Live Server"

### Opção 2: Python HTTP Server
```bash
cd "/home/abraao/Downloads/OASIS_FRONT_END"
python -m http.server 8000
```
Abra: **http://localhost:8000**

### Opção 3: Node HTTP Server
```bash
cd "/home/abraao/Downloads/OASIS_FRONT_END"
npx http-server -p 8000
```

---

## 4️⃣ Teste no Front-End

### Passo 1: Abra o Console do Navegador (F12)

### Passo 2: Teste a API diretamente
```javascript
// Listar categorias
API.getCategories().then(r => console.log(r));

// Criar hábito
API.createHabit({
  titulo: 'Exercício',
  descricao: 'Treino de 30 minutos',
  categoria: 'cat_saude',
  frequencia: 1,
  user_id: 1
}).then(r => console.log(r));

// Listar hábitos do usuário
API.getHabitsByUser(1).then(r => console.log(r));

// Toggle hábito
API.toggleHabitComplete(1).then(r => console.log(r));
```

### Passo 3: Teste Visualmente
1. Clique em "Novo Hábito"
2. Preencha o formulário
3. Salve
4. Verifique se aparece na lista
5. Clique no checkbox para completar

---

## 5️⃣ Arquivos Importantes

### Backend
```
oasis_backend/
├── app.py                          # Aplicação principal
├── app/routes/                     # Rotas da API
│   ├── auth.py                     # Login/Signup
│   ├── habits.py                   # CRUD Hábitos
│   ├── categories.py               # CRUD Categorias
│   └── journal.py                  # CRUD Diário
├── app/services/                   # Lógica de negócio
│   ├── user_service.py
│   ├── habit_service.py
│   ├── category_service.py
│   └── journal_service.py
├── data/                           # Armazenamento JSON
│   ├── users.json
│   ├── habitos.json
│   ├── categorias.json
│   ├── categorias_usuario.json
│   └── registros_diarios.json
├── ENDPOINTS_SUMMARY.md            # Todos os endpoints
└── INTEGRATION_GUIDE.md            # Guia completo
```

### Front-End
```
OASIS_FRONT_END/
├── index.html                      # UI Principal
├── api.js                          # ⭐ Serviço de API (NOVO)
├── app.js                          # Lógica da aplicação
├── styles.css                      # Estilos
└── INTEGRATION_GUIDE.md            # ⭐ Guia de integração (NOVO)
```

---

## 🐛 Troubleshooting

### Erro: "Failed to fetch"
✅ **Solução:** Certifique-se de que o backend está rodando em `http://localhost:5000`

### Erro: CORS
✅ **Solução:** CORS já está configurado. Verifique se está usando `http://localhost` (não file://)

### Erro: "categoria é obrigatória"
✅ **Solução:** Use um dos IDs de categoria padrão:
- `cat_saude`
- `cat_produtividade`
- `cat_aprendizado`
- `cat_bem_estar`
- `cat_social`
- `cat_financeiro`
- `cat_criatividade`
- `cat_outros`

### Dados não aparecem
✅ **Solução:** 
1. Abra o console (F12)
2. Verifique erros de rede
3. Confirme que `user_id: 1` existe

---

## 📋 Checklist de Verificação

Backend:
- [ ] Servidor rodando em http://localhost:5000
- [ ] GET / retorna JSON com endpoints
- [ ] GET /api/categories retorna 8 categorias
- [ ] POST /api/signup cria usuário
- [ ] POST /api/habits cria hábito

Front-End:
- [ ] api.js carregado antes de app.js
- [ ] Console não mostra erros
- [ ] Consegue criar hábito pela interface
- [ ] Hábito aparece na lista
- [ ] Toggle funciona

---

## 📚 Documentação Completa

- **ENDPOINTS_SUMMARY.md** - Referência de todos os endpoints
- **INTEGRATION_GUIDE.md** (front-end) - Como modificar app.js
- **API_DOCS.md** - Documentação detalhada da API
- **INTEGRACAO_COMPLETA.md** - Visão geral completa

---

**Tudo pronto para desenvolvimento! 🎉**

Se tiver dúvidas, consulte `INTEGRATION_GUIDE.md` no front-end ou `ENDPOINTS_SUMMARY.md` no backend.
