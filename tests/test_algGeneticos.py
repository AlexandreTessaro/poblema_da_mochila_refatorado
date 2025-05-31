import pytest
import sys
import os

# Garante que o diretório raiz seja reconhecido para os imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algoritmos.algGeneticos import (
    gerar_instancia_aleatoria,
    gerar_individuo,
    avaliar_individuo,
    selecao,
    crossover,
    mutacao,
    algoritmo_genetico
)

def test_gerar_instancia_aleatoria():
    pesos, valores, capacidade = gerar_instancia_aleatoria(5)
    assert isinstance(pesos, list)
    assert isinstance(valores, list)
    assert isinstance(capacidade, int)
    assert len(pesos) == 5
    assert len(valores) == 5
    assert capacidade > 0

def test_gerar_individuo():
    individuo = gerar_individuo(10)
    assert isinstance(individuo, list)
    assert len(individuo) == 10
    assert all(gene in (0, 1) for gene in individuo)

def test_avaliar_individuo_sem_excesso():
    pesos = [1, 2, 3]
    valores = [10, 20, 30]
    capacidade = 6
    individuo = [1, 1, 0]  # peso = 3, valor = 30
    resultado = avaliar_individuo(individuo, pesos, valores, capacidade)
    assert resultado == 30

def test_avaliar_individuo_com_excesso():
    pesos = [5, 5, 5]
    valores = [10, 20, 30]
    capacidade = 10
    individuo = [1, 1, 1]  # peso = 15, valor = 60 → penalizado
    resultado = avaliar_individuo(individuo, pesos, valores, capacidade)
    assert resultado == 50  # penalização de 10

def test_selecao_retorna_dois_individuos():
    pesos, valores, capacidade = gerar_instancia_aleatoria(10)
    populacao = [gerar_individuo(10) for _ in range(10)]
    pai1, pai2 = selecao(populacao, pesos, valores, capacidade)
    assert isinstance(pai1, list) and isinstance(pai2, list)
    assert len(pai1) == 10 and len(pai2) == 10
    assert all(g in (0, 1) for g in pai1 + pai2)

def test_crossover():
    pai1 = [1, 1, 1, 1]
    pai2 = [0, 0, 0, 0]
    filho1, filho2 = crossover(pai1, pai2)
    assert isinstance(filho1, list) and isinstance(filho2, list)
    assert len(filho1) == 4 and len(filho2) == 4
    assert filho1 != pai1 or filho2 != pai2  # deve haver mudança

def test_mutacao():
    individuo = [0, 0, 0, 0]
    mutado = mutacao(individuo[:], taxa_mutacao=1.0)  # força a mutação total
    assert mutado == [1, 1, 1, 1]

def test_algoritmo_genetico_executa():
    pesos, valores, capacidade = gerar_instancia_aleatoria(10)
    solucao, valor, peso = algoritmo_genetico(pesos, valores, capacidade, tam_populacao=10, n_geracoes=10)
    assert isinstance(solucao, list)
    assert all(g in (0, 1) for g in solucao)
    assert isinstance(valor, (int, float))
    assert isinstance(peso, (int, float))
    assert sum(p * s for p, s in zip(pesos, solucao)) == peso
