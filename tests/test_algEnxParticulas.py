import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algoritmos.algEnxParticulas import (
    sigmoid,
    Particula,
    pso
)

from utils.geracao import gerar_instancia_aleatoria
from utils.avalicao import avaliar


def test_gerar_dados():
    pesos, valores, capacidade = gerar_instancia_aleatoria(10)
    assert len(pesos) == 10
    assert len(valores) == 10
    assert isinstance(capacidade, int)
    assert capacidade > 0

def test_sigmoid():
    assert round(sigmoid(0), 5) == 0.5
    assert sigmoid(10) > 0.99
    assert sigmoid(-10) < 0.01

def test_avaliar_solucao_valida():
    pesos = [1, 2, 3]
    valores = [10, 20, 30]
    capacidade = 6
    solucao = [1, 1, 0]  # peso total = 3
    valor, _ = avaliar(solucao, pesos, valores, capacidade)
    assert valor == 30

def test_avaliar_solucao_invalida():
    pesos = [4, 4, 4]
    valores = [10, 20, 30]
    capacidade = 5
    solucao = [1, 1, 1]  # peso total = 12
    valor, peso = avaliar(solucao, pesos, valores, capacidade)
    assert valor == 0
    assert peso > capacidade

def test_particula_binarizar():
    p = Particula(3, [1, 2, 3], [10, 20, 30], 5)
    binaria = p.binarizar()
    assert len(binaria) == 3
    assert all(g in [0, 1] for g in binaria)

def test_particula_atualizar_pessoal():
    p = Particula(3, [1, 1, 1], [10, 20, 30], 3)
    valor_antigo = p.best_valor
    p.posicao = [10, 10, 10]  # força ativação completa
    p.atualizar_best_pessoal()
    assert p.best_valor >= valor_antigo

def test_pso_executa():
    pesos, valores, capacidade = gerar_instancia_aleatoria(10)
    solucao, valor, peso = pso(10, pesos, valores, capacidade)
    assert isinstance(solucao, list)
    assert all(g in [0, 1] for g in solucao)
    assert isinstance(valor, (int, float))
    assert isinstance(peso, (int, float))
