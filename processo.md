# 🔄 processo.md — Processo de Refatoração

## 📌 Objetivo

Este documento descreve o processo adotado pela equipe para realizar a refatoração do código recebido, assegurando que o código original não fosse modificado, conforme exigido pelas instruções da atividade.

---

## 🧠 Estratégia de Trabalho

### 1. **Separação do Código Original**

- Criamos uma pasta chamada `original/` dentro do repositório.
- Copiamos o código original da outra equipe exatamente como recebido.
- **Não realizamos nenhuma modificação nesta pasta**.

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
- Commits frequentes foram utilizados para garantir versionamento granular.

---

### 4. **Execução e Validação**

- Criamos o arquivo `main.py` dentro de `bio/` para executar comparações entre os algoritmos refatorados.
- Esse arquivo executa os testes e gera uma tabela com tempos e resultados.
- A saída foi utilizada para validar os comportamentos esperados.

---

### 5. **Testes Automatizados**

- Criamos testes com o framework `pytest`, focando:
  - Soluções válidas (binárias e dentro da capacidade).
  - Avaliação correta de valor/peso.
  - Execução sem erros.
- Os testes rodam automaticamente com o comando:

```bash
pytest tests/
6. Ferramentas de Qualidade
Utilizamos as seguintes ferramentas para garantir qualidade:

Ferramenta	Uso
flake8	Análise de estilo e erros de código
pytest	Criação e execução de testes automatizados
ChatGPT	Sugestões de refatoração e padrões de projeto
Git	Controle de versões e separação entre código refatorado e original

🔒 Garantia de Não-Modificação do Original
A equipe nunca alterou o conteúdo da pasta original/.

Todo o trabalho foi feito de forma independente em refatorado/.

Isso garante total rastreabilidade e preservação do código base.

👥 Organização da Equipe
Divisão de tarefas:

Análise do código: feita em grupo.

Refatoração inicial: responsável principal + revisão do grupo.

Testes e validação: par programação.

Documentação e slides: colaboração em nuvem.

🧠 Aprendizados do Processo
Refatorar com base em técnicas consolidadas aumenta a qualidade do código.

Separar lógica de execução e testes ajuda a manter coesão.

Ferramentas como flake8 e pytest são essenciais no ciclo de desenvolvimento.

A documentação clara do processo é tão importante quanto o código em si.

csharp
Copy
Edit

Se você quiser, posso também gerar os slides da apresentação com base nesse conteúdo. Deseja isso agora?





