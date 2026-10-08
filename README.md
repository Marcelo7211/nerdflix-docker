# Nerdflix Docker

Projeto de exemplo do curso **Docker do zero: containers, Compose e Swarm** (Nerdflix).

É uma loja de filmes pequena, em três partes:

| Parte | Tecnologia | Pasta |
|---|---|---|
| Front-end | HTML, CSS e JavaScript | `frontend/` |
| Back-end (API) | Python com Flask | `backend/` |
| Banco de dados | MySQL | `db/` (script de criação da tabela) |

```
navegador --> Nginx (front) --/api--> API Flask --> MySQL
```

## Como usar no curso

A branch `main` traz **só o código da aplicação**. Os arquivos do Docker (Dockerfile, `docker-compose.yml`,
`docker-stack.yml`, `nginx/default.conf` e `.env`) são escritos por você, aula a aula.

Se travar em algum passo, compare com a branch `solucao`, que tem todos os arquivos prontos:

```bash
git checkout solucao
```

## API

| Método | Rota | O que faz |
|---|---|---|
| GET | `/api/saude` | Devolve `status`, o nome do container que respondeu (`host`) e a `versao` |
| GET | `/api/filmes` | Lista os filmes |
| POST | `/api/filmes` | Cadastra um filme, com JSON `{"titulo": "...", "ano": 2024}` |

A conexão com o banco vem das variáveis de ambiente `DB_HOST`, `DB_USER`, `DB_PASSWORD` e `DB_NAME`.

## Portas usadas no curso

| Serviço | Porta no computador |
|---|---|
| Front (Nginx) | 8088 |
| API | 5050 |
| MySQL | 3307 |
| Registry local | 5001 |

As senhas do curso (`root` e `loja123`) servem **só para estudo**. Em produção, senha nunca vai no código.
