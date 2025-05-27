import pytest
from refatorado.bio.algBeeAlgorithm import bee_algorithm, avaliar_solucao

@pytest.fixture
def instancia_simples():
    pesos = [2, 3, 4, 5]
    valores = [3, 4, 5, 6]
    capacidade = 5
    return pesos, valores, capacidade


def test_avaliar_solucao_dentro_da_capacidade(instancia_simples):
    pesos, valores, capacidade = instancia_simples
    solucao = [1, 0, 0, 0]  # peso 2, valor 3
    valor, peso = avaliar_solucao(solucao, pesos, valores, capacidade)
    assert peso <= capacidade
    assert valor == 3


def test_avaliar_solucao_fora_da_capacidade(instancia_simples):
    pesos, valores, capacidade = instancia_simples
    solucao = [1, 1, 1, 1]  # peso 14 > 5
    valor, peso = avaliar_solucao(solucao, pesos, valores, capacidade)
    assert valor == 0
    assert peso > capacidade


def test_bee_algorithm_resultado_valido(instancia_simples):
    pesos, valores, capacidade = instancia_simples
    solucao, valor, peso = bee_algorithm(pesos, valores, capacidade, n_abelhas=10, n_melhores=5, n_vizinhos=1, n_iter=10)
    
    assert isinstance(solucao, list)
    assert isinstance(valor, int)
    assert isinstance(peso, int)
    assert len(solucao) == len(pesos)
    assert peso <= capacidade
