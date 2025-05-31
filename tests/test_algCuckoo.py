import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algoritmos.algCuckoo import levy_flight, cuckoo_search
from utils.geracao import gerar_instancia_aleatoria, gerar_solucao
from utils.avalicao import avaliar

def test_gerar_instancia_aleatoria():
    pesos, valores, capacidade = gerar_instancia_aleatoria(10)
    assert len(pesos) == 10
    assert len(valores) == 10
    assert isinstance(capacidade, int)
    assert capacidade > 0

def test_gerar_solucao():
    solucao = gerar_solucao(5)
    assert len(solucao) == 5
    assert all(bit in [0, 1] for bit in solucao)

def test_avaliar_solucao_valida():
    pesos = [1, 2, 3]
    valores = [10, 20, 30]
    capacidade = 6
    solucao = [1, 1, 0]  # peso = 3
    valor, peso = avaliar(solucao, pesos, valores, capacidade)
    assert valor == 30
    assert peso == 3

def test_avaliar_solucao_invalida():
    pesos = [4, 5, 6]
    valores = [10, 20, 30]
    capacidade = 5
    solucao = [1, 1, 1]  # peso = 15 > capacidade
    valor, peso = avaliar(solucao, pesos, valores, capacidade)
    assert valor == 0
    assert peso > capacidade

def test_levy_flight_altera_ou_mantem_solucao():
    solucao = [0, 1, 0, 1, 0]
    nova = levy_flight(solucao)
    assert len(nova) == len(solucao)
    assert all(bit in [0, 1] for bit in nova)

def test_cuckoo_search_executa():
    pesos, valores, capacidade = gerar_instancia_aleatoria(10)
    solucao, valor, peso = cuckoo_search(pesos, valores, capacidade, n_ninhos=10, n_iteracoes=10)
    assert isinstance(solucao, list)
    assert isinstance(valor, (int, float))
    assert isinstance(peso, (int, float))
    assert all(bit in [0, 1] for bit in solucao)
