# FastAPI Lab 🚀

Repositório de estudos dedicado à revisão e prática do framework **FastAPI**, acompanhando a trilha do Corey Schafer.

---

## 📺 Módulo 01: Setup e Fundamentos
Baseado no vídeo: [Python FastAPI Tutorial (Part 1)](https://www.youtube.com/watch?v=7AMjmCTumuo)


### Principais pontos:
* **Ambiente:** Setup utilizando `uv` (mais rápido que o pip tradicional) e instalação do `fastapi[standard]`.
* **CLI & Dev Mode:** Uso do `fastapi dev main.py` para aproveitar o *hot reload* durante o desenvolvimento.
* **Rotas & JSON:** Criação de endpoints básicos retornando dicionários que o framework converte automaticamente para JSON.
* **Auto-Doc:** Exploração do Swagger UI (`/docs`) e ReDoc (`/redoc`) para testes rápidos dos endpoints.
* **Dual-Response:** Implementação de `HTMLResponse` para servir páginas simples e uso de `include_in_schema=False` para manter a documentação da API limpa, escondendo as rotas que são apenas para o navegador.
