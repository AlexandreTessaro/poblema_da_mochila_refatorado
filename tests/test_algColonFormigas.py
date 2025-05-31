import sys
import os

# Garante acesso ao diretório raiz e módulos
RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, RAIZ)

from algoritmos.algColonFormigas import aco_knapsack
from utils.geracao import gerar_instancia_aleatoria
from utils.avalicao import avaliar

def test_gerar_instancia_aleatoria():
    pesos, valores, capacidade = gerar_instancia_aleatoria(10)
    assert len(pesos) == 10
    assert len(valores) == 10
    assert isinstance(capacidade, int)
    assert capacidade > 0

def test_avaliar_solucao_valida():
    pesos = [1, 2, 3]
    valores = [10, 20, 30]
    capacidade = 6
    solucao = [1, 1, 0]  # peso = 3
    valor, peso = avaliar(solucao, pesos, valores, capacidade)
    assert valor == 30
    assert peso == 3

def test_avaliar_solucao_invalida():
    pesos = [4, 4, 4]
    valores = [10, 20, 30]
    capacidade = 5
    solucao = [1, 1, 1]  # peso = 12 > capacidade
    valor, peso = avaliar(solucao, pesos, valores, capacidade)
    assert valor == 0
    assert peso > capacidade

def test_aco_knapsack_executa():
    pesos, valores, capacidade = gerar_instancia_aleatoria(15)
    solucao, valor, peso = aco_knapsack(
        pesos, valores, capacidade,
        n_formigas=10, n_iteracoes=10
    )
    assert isinstance(solucao, list)
    assert all(bit in [0, 1] for bit in solucao)
    assert isinstance(valor, (int, float))
    assert isinstance(peso, (int, float))
