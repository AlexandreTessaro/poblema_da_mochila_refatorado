# 📘 Refatoração - Problema da Mochila com Algoritmos Bio-inspirados

## 📌 Introdução

Este documento apresenta o plano e justificativas para a refatoração do projeto original do Problema da Mochila com Algoritmos Bio-inspirados. O código analisado foi produzido por outra equipe e continha diversos pontos de melhoria quanto à estrutura, modularização e qualidade de código.

---

## 🧐 Análise do Código Original

Durante a leitura e execução do código original, foram identificados os seguintes problemas:

* 🔁 **Código duplicado**: cada algoritmo implementava estrutura de testes repetida.
* 🤯 **Falta de coesão**: funções relacionadas estavam espalhadas sem agrupamento lógico.
* 🔗 **Acoplamento excessivo**: testes estavam acoplados diretamente à lógica dos algoritmos.
* ❌ **Ausência de testes unitários**: não havia nenhum tipo de verificação automatizada.
* 🧩 **Nomeação confusa**: nomes de funções e variáveis muitas vezes não eram claros.
* 🧱 **Problemas de estrutura**: o código estava todo em um único arquivo por algoritmo, dificultando reuso.

---

## 🛠️ Planejamento da Refatoração

### Objetivos

* Separar a lógica dos algoritmos de seus testes.
* Tornar os algoritmos reutilizáveis como módulos.
* Facilitar a análise comparativa entre algoritmos.
* Garantir a corretude via testes automatizados.
* Aumentar a legibilidade e manutenibilidade.

### Técnicas Utilizadas

As técnicas foram baseadas no livro **"Refatoração – Aperfeiçoando o Design de Códigos Existentes"** de **Martin Fowler**, bem como nos sites [Refactoring Guru](https://refactoring.guru) e [Refactoring Catalog](https://refactoring.com).

| Técnica                  | Descrição                                              |
| ------------------------ | ------------------------------------------------------ |
| **Extract Function**     | Separação de blocos repetidos em funções reutilizáveis |
| **Move Function**        | Realocação de funções para módulos mais coesos         |
| **Rename Variable**      | Renomeação de variáveis e funções para maior clareza   |
| **Split Phase**          | Separação entre lógica de negócio e entrada/saída      |
| **Encapsulate Variable** | Proteção e organização de atributos em funções         |

---

## ⚙️ Refatorações Realizadas

### Estrutura Anterior (por algoritmo):

algoritmo\_original.py

### Estrutura Refatorada:

refatorado/
│
| bio/
│   | algBeeAlgorithm.py
│   | algColonFormigas.py
│   | algCuckoo.py
│   | algEnxParticulas.py
│   | algGeneticos.py
│   | main.py ← Executa e compara os algoritmos
│   | **init**.py
│
|  tests/
│    | test\_algoritmos.py ← Testes unitários com pytest
│
|   original/ ← Código original da outra equipe
│
|   refatoracao.md
|   processo.md
|   README.md
|   slides\_apresentacao.pdf

---

## ✅ Resultados da Refatoração

| Critério                    | Antes    | Depois                       |
| --------------------------- | -------- | ---------------------------- |
| Modularização               | ❌ Não    | ✅ Sim                        |
| Reutilização de código      | ❌ Pouca  | ✅ Alta                       |
| Testes unitários            | ❌ Nenhum | ✅ Presentes                  |
| Legibilidade                | 😕 Baixa | 😀 Alta                      |
| Comparação entre algoritmos | ❌ Manual | ✅ Automatizada via `main.py` |
| Tempo de execução medido    | ❌ Não    | ✅ Sim                        |

---

## 🧪 Testes

Criamos testes usando o `pytest` para garantir que os algoritmos:

* Geram uma solução válida.
* Não excedem a capacidade da mochila.
* Mantêm o valor máximo possível dentro da restrição.

Os testes estão localizados em `tests/test_algoritmos.py`.

---

## 📚 Referências

* Fowler, Martin. *Refatoração: Aperfeiçoando o Design de Códigos Existentes.*
* Refactoring Guru: [https://refactoring.guru](https://refactoring.guru)
* Refactoring Catalog: [https://refactoring.com](https://refactoring.com)
* Pytest: [https://docs.pytest.org](https://docs.pytest.org)
* PEP8 + flake8: [https://flake8.pycqa.org](https://flake8.pycqa.org)

---

## 🤖 IA como Apoio

Utilizamos **ChatGPT** como ferramenta de apoio para:

* Sugerir boas práticas.
* Explicar padrões de refatoração.
* Gerar esboços de testes e código limpo.

---

## 🧠 Aprendizados

* Refatorar é mais que reescrever: exige análise e justificativa.
* A modularização facilita testes e comparações.
* A separação entre lógica e execução torna o código escalável.
* A análise estática (com `flake8`) ajuda a manter qualidade contínua.

---
