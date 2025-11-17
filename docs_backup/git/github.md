# Git vs GitHub: Entendendo as Diferenças

## O que é Git?

**Git** é um sistema de controle de versão distribuído, criado por Linus Torvalds em 2005. É uma ferramenta de linha de comando que permite rastrear alterações no código-fonte ao longo do tempo.

### Características principais do Git:
- **Local**: Funciona completamente no seu computador
- **Controle de versão**: Mantém histórico completo de todas as alterações
- **Distribuído**: Cada desenvolvedor tem uma cópia completa do repositório
- **Gratuito e open-source**: Software livre para uso
- **Offline**: Funciona sem conexão com a internet

### O que o Git faz?
- Rastreia mudanças em arquivos
- Permite reverter para versões anteriores
- Possibilita trabalhar em diferentes versões (branches) simultaneamente
- Facilita a colaboração entre desenvolvedores
- Mantém histórico detalhado de quem fez o quê e quando

---

## O que é GitHub?

**GitHub** é uma plataforma de hospedagem de código baseada na web que usa Git. Foi criada em 2008 e adquirida pela Microsoft em 2018.

### Características principais do GitHub:
- **Baseado na nuvem**: Armazena repositórios online
- **Interface gráfica**: Facilita visualização e gerenciamento de código
- **Colaboração**: Ferramentas para trabalho em equipe
- **Social**: Permite seguir desenvolvedores e projetos
- **Integração**: Conecta com diversas ferramentas de desenvolvimento

### O que o GitHub faz?
- Hospeda repositórios Git remotamente
- Facilita colaboração através de Pull Requests
- Oferece sistema de Issues para rastreamento de bugs e tarefas
- Fornece GitHub Actions para automação (CI/CD)
- Permite documentação via GitHub Pages
- Oferece controle de acesso e permissões

---

## Diferenças Principais

| Aspecto | Git | GitHub |
|---------|-----|--------|
| **Tipo** | Software/Ferramenta | Serviço/Plataforma |
| **Localização** | Local (seu computador) | Nuvem (internet) |
| **Interface** | Linha de comando | Web + Git |
| **Custo** | Gratuito | Gratuito + planos pagos |
| **Função** | Controle de versão | Hospedagem + colaboração |
| **Dependência** | Independente | Depende do Git |

---

## Alternativas ao GitHub

Embora o GitHub seja popular, existem outras plataformas similares:
- **GitLab**: Plataforma completa com CI/CD integrado
- **Bitbucket**: Da Atlassian, integra com Jira
- **Gitea**: Solução self-hosted leve
- **SourceForge**: Uma das mais antigas plataformas

---

## Comandos Git Básicos

### Configuração Inicial
```bash
# Configurar nome de usuário
git config --global user.name "Seu Nome"

# Configurar email
git config --global user.email "seu@email.com"

# Verificar configurações
git config --list
```

### Criando e Clonando Repositórios
```bash
# Inicializar novo repositório local
git init

# Clonar repositório existente
git clone https://github.com/usuario/repositorio.git

# Clonar para pasta específica
git clone https://github.com/usuario/repositorio.git nome-da-pasta
```

### Trabalhando com Alterações
```bash
# Verificar status dos arquivos
git status

# Adicionar arquivo específico ao staging
git add arquivo.txt

# Adicionar todos os arquivos modificados
git add .

# Adicionar todos os arquivos de um tipo
git add *.js

# Fazer commit das alterações
git commit -m "Mensagem descritiva do commit"

# Adicionar e commitar em um comando
git commit -am "Mensagem do commit"
```

### Branches (Ramificações)
```bash
# Listar branches
git branch

# Criar nova branch
git branch nome-da-branch

# Mudar para outra branch
git checkout nome-da-branch

# Criar e mudar para nova branch
git checkout -b nova-branch

# Deletar branch local
git branch -d nome-da-branch

# Mesclar branch na atual
git merge nome-da-branch
```

### Sincronização com Repositório Remoto
```bash
# Adicionar repositório remoto
git remote add origin https://github.com/usuario/repositorio.git

# Verificar repositórios remotos
git remote -v

# Enviar alterações para o remoto
git push origin main

# Enviar e configurar upstream
git push -u origin main

# Baixar alterações do remoto
git pull origin main

# Buscar alterações sem mesclar
git fetch origin
```

### Histórico e Informações
```bash
# Ver histórico de commits
git log

# Ver histórico resumido
git log --oneline

# Ver histórico com gráfico
git log --graph --oneline --all

# Ver alterações em arquivo específico
git log -p arquivo.txt

# Ver diferenças não commitadas
git diff

# Ver diferenças do staging
git diff --staged
```

### Desfazendo Alterações
```bash
# Descartar alterações em arquivo
git checkout -- arquivo.txt

# Remover arquivo do staging
git reset arquivo.txt

# Desfazer último commit (mantém alterações)
git reset --soft HEAD~1

# Desfazer último commit (descarta alterações)
git reset --hard HEAD~1

# Reverter commit criando novo commit
git revert <hash-do-commit>
```

### Outras Operações Úteis
```bash
# Ver quem modificou cada linha
git blame arquivo.txt

# Salvar alterações temporariamente
git stash

# Recuperar alterações salvas
git stash pop

# Listar stashes
git stash list

# Criar tag
git tag v1.0.0

# Enviar tags para remoto
git push --tags
```

---

## Fluxo de Trabalho Básico

1. **Clone ou inicialize** um repositório
2. **Crie uma branch** para sua feature/correção
3. **Faça alterações** nos arquivos
4. **Adicione** as alterações ao staging (`git add`)
5. **Commit** suas mudanças com mensagem descritiva
6. **Push** para o repositório remoto
7. **Crie um Pull Request** no GitHub (se trabalhando em equipe)
8. **Merge** após revisão e aprovação

---

## Boas Práticas

### Commits
- Faça commits pequenos e frequentes
- Use mensagens claras e descritivas
- Comece mensagens com verbo no imperativo (ex: "Adiciona", "Corrige", "Remove")

### Branches
- Use branch `main` ou `master` para código estável
- Crie branches para cada feature ou correção
- Use nomes descritivos: `feature/login`, `bugfix/menu`

### Colaboração
- Sempre faça `pull` antes de começar a trabalhar
- Resolva conflitos cuidadosamente
- Revise código de outros desenvolvedores
- Mantenha o README.md atualizado

---

## Recursos Adicionais

- **Documentação oficial do Git**: https://git-scm.com/doc
- **GitHub Docs**: https://docs.github.com
- **Git Cheat Sheet**: https://education.github.com/git-cheat-sheet-education.pdf
- **Aprenda Git Interativamente**: https://learngitbranching.js.org

---

## Conclusão

Git e GitHub são ferramentas complementares essenciais no desenvolvimento moderno. Enquanto o Git gerencia versões do seu código localmente, o GitHub facilita a colaboração e hospedagem. Dominar ambos é fundamental para qualquer desenvolvedor.