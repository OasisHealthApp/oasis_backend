OASIS - Backend (API)

Visão geral

Este repositório contém a API do OASIS (desenvolvimento). A documentação original foi consolidada neste README e os arquivos antigos foram movidos para `docs_backup/` para referência.

Principais conceitos

- Autenticação: JWT com expiração (login/signup endpoints).
- Recursos principais: Habits (hábitos), Categories (categorias), Journal (registros diários), Users.
- Persistência em desenvolvimento: arquivos JSON em `data/`.

Endpoints principais (resumo)

Base: /api

Auth
- POST /api/login
  - Payload: { "email": "user@example.com", "senha": "password" }
  - Retorna: { token, usuario: { id, nome, email } }

- POST /api/signup
  - Payload: { "nome", "email", "senha" }

Users
- GET /api/users

Habits
- GET /api/habits
- GET /api/habits/user/<user_id>
- POST /api/habits
  - Payload exemplo: { "titulo": "Meditar", "descricao": "10 min", "categoria": 1, "repetir": true, "tipo_repeticao": "diario", "user_id": 1 }
- PUT /api/habits/<id>
- DELETE /api/habits/<id>
- POST /api/habits/<id>/toggle  (ou similar) - alterna completado

Categories
- GET /api/categories
- GET /api/categories?user_id=<id>
- POST /api/categories
- PUT /api/categories/<id>
- DELETE /api/categories/<id>

Journal
- GET /api/journal
- GET /api/journal/user/<user_id>
- GET /api/journal/user/<user_id>/date/<YYYY-MM-DD>
  - Nota: agora retorna lista de registros para a data (várias entradas permitidas)
- POST /api/journal
  - Payload: { "conteudo": "texto", "user_id": 1, "data": "YYYY-MM-DD" }
- PUT /api/journal/<id>
- DELETE /api/journal/<id>

Como integrar (rápido)

- Autentique via /api/login para obter token (Bearer). O frontend usa `localStorage` para armazenar token e `usuario`.
- Inclua o token no header Authorization quando necessário: `Authorization: Bearer <token>`.

Exemplos de fluxo

1. Signup -> Login -> Criar categoria -> Criar hábito -> Marcar hábito concluído -> Registrar diário
2. Para repetição mensal, o backend utiliza lógica baseada em `relativedelta` para lidar corretamente com meses com menos dias (ex.: fevereiro).

Operações de criação/atualização/remoção

- Criação: POST com JSON no corpo. Retorna 201 quando criado.
- Atualização: PUT com JSON. Retorna 200 quando atualizado.
- Remoção: DELETE no recurso. Retorna 200 quando excluído.

Observações sobre dados

- Em ambiente de desenvolvimento os dados ficam em `data/*.json` (users.json, habitos.json, categorias.json, registros_diarios.json).
- Faça backup desses arquivos antes de mudanças manuais.

Local de referência

Arquivos originais movidos para `docs_backup/` no repositório para referência histórica (não apagados).

Contribuição / execução local

1. Ative o virtualenv: `source OasisVenv/bin/activate` (ou crie um).
2. Instale dependências (requirements.txt) se necessário.
3. Rode: `python app.py` (ou use um servidor WSGI para produção).

--
Este README sintetiza a documentação principal para facilitar integração e uso rápido da API. Arquivos mais detalhados permanecem em `docs_backup/`.
