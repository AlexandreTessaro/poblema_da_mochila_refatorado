# Refatoração do Problema da Mochila com Algoritmos Bio-inspirados

## Descrição do Projeto

Este projeto consiste na implementação e refatoração de diversas soluções bio-inspiradas para o Problema da Mochila 0/1, utilizando algoritmos como Bee Algorithm, Algoritmo Genético, Particle Swarm Optimization (PSO), Cuckoo Search e Ant Colony Optimization (ACO).  
O objetivo é fornecer uma estrutura modular, clara e reutilizável que permita executar, comparar e analisar o desempenho de cada algoritmo sobre diferentes instâncias do problema.

---

## Estrutura do Projeto

poblema_da_mochila_refatorado/
│
├── refatorado/
│ ├── bio/
│ │ ├── algBeeAlgorithm.py # Implementação do Bee Algorithm
│ │ ├── algGeneticos.py # Implementação do Algoritmo Genético
│ │ ├── algEnxParticulas.py # Implementação do PSO
│ │ ├── algCuckoo.py # Implementação do Cuckoo Search
│ │ ├── algColonFormigas.py # Implementação do ACO
│ │ ├── main.py # Script principal para executar e comparar os algoritmos
│ │ └── tests/ # Testes unitários para cada algoritmo
│ │ ├── test_algGeneticos.py
│ │ ├── test_bee.py
│ │ ├── test_cuckoo.py
│ │ └── test_pso.py
│
└── README.md # Este arquivo

markdown
Copy
Edit

---

## Implementação dos Algoritmos

Cada arquivo `.py` dentro da pasta `bio/` contém uma implementação completa do respectivo algoritmo, com as seguintes características:

- **Entrada:** listas de pesos, valores dos itens e capacidade da mochila.
- **Saída:** melhor solução encontrada (lista binária), valor total e peso total da mochila.
- **Função principal:** `main()` ou função similar que executa o algoritmo em instâncias de teste e retorna resultados em um formato padronizado (`pandas.DataFrame` ou lista de dicionários).

### Algoritmos Implementados

- `algBeeAlgorithm.py` — Bee Algorithm, inspirado no comportamento das abelhas na busca por soluções.
- `algGeneticos.py` — Algoritmo Genético, baseado em seleção, cruzamento e mutação.
- `algEnxParticulas.py` — Particle Swarm Optimization, simula o comportamento coletivo de enxames.
- `algCuckoo.py` — Cuckoo Search, inspirado no comportamento de reprodução de algumas espécies de cucos.
- `algColonFormigas.py` — Ant Colony Optimization, inspirado no caminho deixado por formigas para encontrar comida.

---

## Arquivo main.py

O `main.py` importa todos os algoritmos, executa suas funções principais e coleta os resultados em `pandas.DataFrame`.  
Após a execução, os resultados são concatenados, organizados e exibidos em formato tabular, comparando o tempo de execução dos algoritmos em diferentes tamanhos de problema.

### Como executar:

```bash
python main.py
O output esperado é um DataFrame pandas contendo:

Número de itens (n_itens)

Tempo de execução de cada algoritmo (Bee Algorithm, Algoritmo Genético, PSO, etc.)

Testes Unitários
Cada algoritmo possui um conjunto de testes unitários implementados na pasta tests/. Eles garantem que:

O algoritmo retorna soluções dentro da capacidade da mochila.

As soluções possuem valor coerente.

O código está livre de erros básicos e mantém a lógica correta.

Como executar os testes:
Se você usa pytest, execute:

bash
Copy
Edit
pytest tests/
Dificuldades e Aprendizados
Integração entre módulos: Foi necessário padronizar os retornos e a estrutura dos dados para permitir concatenação e análise conjunta.

Importação e estrutura do projeto: Ajustar caminhos e pacotes para evitar erros de importação foi essencial para a execução fluida do projeto.

Padronização dos nomes dos algoritmos: Para pivotar os dados e comparar, foi necessário garantir que os nomes fossem idênticos em todos os módulos.

Gerenciamento de instâncias: Criação de funções para gerar instâncias aleatórias de forma consistente, mantendo variabilidade de testes.

Documentação e legibilidade: Refatorar para deixar o código mais limpo, legível e modular.

Teste em larga escala: Rodar algoritmos com instâncias muito grandes para verificar desempenho e estabilidade.

Tecnologias e Bibliotecas Utilizadas
Python 3.13+

Pandas: para manipulação e análise de dados.

pytest: framework para testes unitários.

Bibliotecas padrão: random, time, typing.

Contato
Alexandre Tessaro 

Qualquer dúvida ou sugestão, fico à disposição!

---