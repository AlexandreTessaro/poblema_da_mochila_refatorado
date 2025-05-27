# 🔄 processo.md — Processo de Refatoração

## 📌 Objetivo

Este documento descreve o processo adotado pela equipe para realizar a refatoração do código recebido, assegurando que o código original não fosse modificado, conforme exigido pelas instruções da atividade.

---

## 🧠 Estratégia de Trabalho

### 1. **Separação do Código Original**

- Criamos uma pasta chamada `original/` dentro do repositório.
- Copiamos o código original da outra equipe exatamente como recebido.
- **Não realizamos nenhuma modificação nesta pasta.**

---

### 2. **Criação de Estrutura Refatorada**

- Criamos uma nova pasta chamada `refatorado/`, com subpastas organizadas por tema:
  - `bio/`: onde estão os algoritmos refatorados.
  - `tests/`: onde estão os testes automatizados criados com `pytest`.
- Todo o desenvolvimento foi feito nesta estrutura, isolando completamente o original.

---

### 3. **Controle de Versão**

- Utilizamos **Git** com uma estrutura de repositório separada.
- Toda a refatoração foi feita em um **novo repositório** independente.
- Commits frequentes foram utilizados para garantir versionamento granular e rastreável.

---

### 4. **Execução e Validação**

- Criamos o arquivo `main.py` dentro de `bio/` para executar comparações entre os algoritmos refatorados.
- Esse arquivo executa os algoritmos e gera uma tabela com tempos de execução e resultados.
- A saída foi utilizada para validar os comportamentos esperados, garantindo que as refatorações mantiveram a lógica original.

---

### 5. **Testes Automatizados**

- Criamos testes com o framework `pytest`, focando em:
  - Soluções válidas (binárias e dentro da capacidade da mochila).
  - Avaliação correta de valor/peso dos itens selecionados.
  - Execução sem erros e com retorno consistente.
- Os testes são executados com o comando:

```bash
pytest tests/
```

---

### 6. **Ferramentas de Qualidade**

Utilizamos as seguintes ferramentas para garantir a qualidade do código:

| Ferramenta | Uso |
|------------|-----|
| **flake8** | Análise de estilo e detecção de erros de sintaxe |
| **pytest** | Criação e execução de testes automatizados |
| **ChatGPT** | Apoio na refatoração, padrões de projeto e boas práticas |
| **Git** | Controle de versão e separação entre código refatorado e original |

---

## 🔒 Garantia de Não-Modificação do Original

- A equipe **nunca alterou o conteúdo da pasta `original/`**.
- Todo o trabalho foi feito de forma independente em `refatorado/`.
- Isso garante **total rastreabilidade e preservação do código base**.

---

## 👥 Organização da Equipe

Divisão de tarefas realizada da seguinte forma:

| Atividade                 | Responsável           |
|---------------------------|------------------------|
| Análise do código         | Toda a equipe          |
| Refatoração inicial       | Membro responsável     |
| Revisão da refatoração    | Coletiva               |
| Testes e validação        | Programação em par     |
| Documentação e slides     | Colaboração em nuvem   |

---

## 🧠 Aprendizados do Processo

- Refatorar com base em técnicas consolidadas aumenta a qualidade do código.
- Separar lógica, testes e execução facilita manutenções futuras.
- Ferramentas como `flake8` e `pytest` são fundamentais no ciclo de desenvolvimento.
- Documentar o processo com clareza é tão importante quanto o código em si.

---
