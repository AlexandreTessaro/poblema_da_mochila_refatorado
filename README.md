# 🎒 Problema da Mochila 0/1 com Algoritmos Bio-inspirados — Refatoração

Este repositório contém a **refatoração do código** do Problema da Mochila 0/1 utilizando **algoritmos bio-inspirados**, realizada conforme as exigências da atividade prática da disciplina.

---

## 📁 Estrutura do Repositório

```
.
├── original/               # Código original (não modificado)
├── refatorado/
│   ├── bio/                # Implementações refatoradas dos algoritmos
│   ├── tests/              # Testes automatizados com pytest
│   ├── main.py             # Script principal para execução e comparação
│   ├── requirements.txt    # Bibliotecas utilizadas
│   ├── refatoracao.md      # Documento explicando todas as melhorias
│   ├── processo.md         # Estratégia de trabalho da equipe
├── README.md               # Este arquivo
└── slides_apresentacao.pptx# Slides usados na apresentação
```

---

## 🧬 Algoritmos Bio-inspirados Refatorados

| Algoritmo               | Descrição                                                  |
| ----------------------- | ---------------------------------------------------------- |
| Bee Algorithm 🐝        | Inspiração em comportamento de abelhas na coleta de néctar |
| Algoritmo Genético 🧬   | Seleção natural, cruzamento e mutação de soluções          |
| Cuckoo Search 🥚        | Baseado no parasitismo de ninhos das aves cuco             |
| PSO (Particle Swarm) 🐦 | Modela o comportamento coletivo de bandos de pássaros      |
| ACO (Ant Colony) 🐜     | Simula o comportamento de formigas em busca de comida      |

Cada algoritmo foi modularizado com responsabilidade única e testes independentes.

---

## ▶️ Como Executar

1. **Clone o repositório**:

```bash
git clone https://github.com/sua-equipe/problema-mochila-refatorado.git
cd problema-mochila-refatorado/refatorado
```

2. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

3. **Execute a comparação entre algoritmos**:

```bash
python main.py
```

A saída será uma tabela com tempo de execução, valor total e peso total de cada algoritmo para diferentes tamanhos de instâncias.

---

## 🦪 Como Rodar os Testes

Dentro da pasta `refatorado/`, execute:

```bash
pytest tests/
```

Os testes validam:

* Correção da avaliação de soluções.
* Limite de capacidade respeitado.
* Execução dos algoritmos sem erro.
* Tipagem e retorno esperado das funções.

---

## 📊 Resultados da Refatoração

* **Código modularizado**, com responsabilidades únicas e separadas por algoritmo.
* **Nomeação adequada** para variáveis e funções, refletindo suas responsabilidades.
* **Remoção de código duplicado** entre algoritmos.
* **Criação de testes automatizados** com `pytest`.
* **Documentação clara** do processo (`refatoracao.md` e `processo.md`).
* **Análise de qualidade** realizada com `flake8`.

---

## 🧠 Aprendizados

* A importância da legibilidade e coesão no código.
* Como aplicar padrões de refatoração reais (extraídos de Martin Fowler, Refactoring Guru).
* O valor da automação de testes para garantir integridade do sistema.
* Como trabalhar em equipe com versionamento, documentação e divisão de responsabilidades.

---

## 📚 Referências

* *Refatoração: Aperfeiçoando o Design de Códigos Existentes* — Martin Fowler
* [Refactoring Guru](https://refactoring.guru/)
* [Refactoring Catalog](https://refactoring.com/catalog/)
* Algoritmos Bioinspirados: Natureza como Computação

---

## 👨‍💼 Equipe

* Alexandre Tessaro Vieira
* Edson Borges Polucena
* Leonardo Pereira Borges
* Richard Schmitz Riedo
* Wuelliton Christian Dos Santos

---

## 📾 Licença

Projeto acadêmico, sem fins lucrativos, desenvolvido com fins didáticos.
