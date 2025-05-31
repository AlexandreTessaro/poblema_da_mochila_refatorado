import sys
import os

# Garante que o diretório raiz (onde está 'utils' e 'algoritmos') seja reconhecido
RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, RAIZ)

from algoritmos.algBeeAlgorithm import (
    gerar_vizinho,
    bee_algorithm,
)

from utils.geracao import gerar_instancia_aleatoria, gerar_solucao
from utils.avalicao import avaliar

def test_gerar_solucao():
    solucao = gerar_solucao(10)
    assert len(solucao) == 10
    assert all(bit in [0, 1] for bit in solucao)

def test_gerar_vizinho_altera_1_bit():
    original = [1, 1, 1, 1, 1]
    vizinho = gerar_vizinho(original)
    assert len(vizinho) == len(original)
    assert sum(o != v for o, v in zip(original, vizinho)) == 1

def test_avaliar_solucao_valida():
    pesos = [2, 3, 4]
    valores = [10, 20, 30]
    capacidade = 6
    solucao = [1, 1, 0]  # peso = 5
    valor, peso = avaliar(solucao, pesos, valores, capacidade)
    assert valor == 30
    assert peso == 5

def test_avaliar_solucao_invalida():
    pesos = [5, 5, 5]
    valores = [10, 20, 30]
    capacidade = 10
    solucao = [1, 1, 1]  # peso = 15
    valor, peso = avaliar(solucao, pesos, valores, capacidade)
    assert valor == 0
    assert peso > capacidade

def test_gerar_instancia_aleatoria():
    pesos, valores, capacidade = gerar_instancia_aleatoria(15)
    assert len(pesos) == 15
    assert len(valores) == 15
    assert isinstance(capacidade, int)
    assert capacidade > 0

def test_bee_algorithm_executa():
    pesos, valores, capacidade = gerar_instancia_aleatoria(10)
    solucao, valor, peso = bee_algorithm(
        pesos, valores, capacidade,
        n_abelhas=10, n_melhores=3, n_vizinhos=2, n_iter=5
    )
    assert isinstance(solucao, list)
    assert all(bit in [0, 1] for bit in solucao)
    assert isinstance(valor, (int, float))
    assert isinstance(peso, (int, float))
