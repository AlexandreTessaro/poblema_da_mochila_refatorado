
# 📦 Refatoração do Algoritmo Bio-inspirado (Bee Algorithm)

## 🔍 Objetivo da Refatoração

O objetivo foi **melhorar a legibilidade, modularidade, manutenibilidade e testabilidade** do código do algoritmo Bee aplicado ao Problema da Mochila 0/1. As refatorações foram guiadas por boas práticas de engenharia de software e técnicas do catálogo de Martin Fowler, Refactoring Guru e Refactoring Catalog.

---

## 1. ✏️ Renomeação de Variáveis e Funções

**Antes**:  
Nomes genéricos e pouco descritivos, como `trial`, `limit`, `scout()`.

**Depois**:  
Nomes mais expressivos como `trial_counters`, `limit_trials`, `generate_scout_bees()`.

**Motivo**:  
Aplicamos as técnicas **Rename Variable** e **Rename Method** para tornar o código mais autoexplicativo.

**Exemplo Prático**:

Antes:
```python
def scout():
    for i in range(num_bees):
        if trial[i] > limit:
            solution[i] = generate_random_solution()
```

Depois:
```python
def generate_scout_bees():
    for i in range(number_of_bees):
        if trial_counters[i] > limit_trials:
            bee_solutions[i] = generate_random_solution()
```

---

## 2. 🧱 Extração de Funções

**O que foi feito**:  
Funções extensas foram divididas em unidades menores como:

- `calculate_fitness()`
- `select_best_sources()`
- `generate_neighbor()`

**Motivo**:  
Utilizamos **Extract Method** para **quebrar responsabilidades**, facilitando testes e reutilização de código.

**Exemplo**:

Antes:
```python
# Tudo junto na main loop
total_weight = sum(items[i]['weight'] for i in solution)
total_value = sum(items[i]['value'] for i in solution)
if total_weight > max_weight:
    fitness = 0
else:
    fitness = total_value
```

Depois:
```python
def calculate_fitness(solution, items, max_weight):
    total_weight = sum(items[i]['weight'] for i in solution)
    total_value = sum(items[i]['value'] for i in solution)
    if total_weight > max_weight:
        return 0
    return total_value
```

---

## 3. 🧭 Isolamento de Responsabilidades

**O que foi feito**:

- Criamos uma **classe `Bee`** para encapsular atributos como `posição`, `valor`, `peso`, `aptidão`.
- **Separamos a lógica do algoritmo** da parte de **leitura de dados** e da **configuração de parâmetros**.

**Motivo**:  
Aplicamos **Move Method** e **Encapsulate Variable** para tornar o código mais **orientado a objetos** e com **baixa acoplagem**.

**Exemplo**:

```python
class Bee:
    def __init__(self, solution, fitness):
        self.solution = solution
        self.fitness = fitness
```

---

## 4. ⚙️ Centralização de Parâmetros e Configurações

**O que foi feito**:

- Centralizamos os parâmetros em um dicionário `config` ou estrutura equivalente.

**Motivo**:  
Melhorar a reutilização e tornar o código mais configurável. Técnica: **Introduce Parameter Object**.

**Exemplo**:

```python
config = {
    "num_bees": 50,
    "num_iterations": 100,
    "limit_trials": 10,
    "neighborhood_size": 5,
    "max_weight": 50
}
```

---

## 5. ✅ Testes Automatizados com pytest

**O que foi feito**:

- Adicionamos testes unitários para funções como `calculate_fitness()` e `is_valid_solution()`.

**Motivo**:  
Usamos **TDD reverso** (teste após refatoração) para garantir que o comportamento original foi mantido.

**Exemplo**: `test_algorithm.py`

```python
def test_fitness_valid_solution(sample_items):
    solution = [0, 1]
    assert calculate_fitness(solution, sample_items, max_weight=50) == 160
```

---

## 📌 Conclusão

As refatorações aplicadas:

- Tornaram o código **mais legível e compreensível**;
- Melhoraram a **organização e modularidade**;
- Facilitam **testes, manutenção e reuso** do algoritmo;
- Preparam o projeto para possíveis **extensões futuras**.

---
