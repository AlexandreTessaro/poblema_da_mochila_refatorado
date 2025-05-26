import random
import time
from typing import List, Tuple


def avaliar_solucao(solucao: List[int], pesos: List[int], valores: List[int], capacidade: int) -> Tuple[int, int]:
    """
    Avalia a solução calculando o valor e peso total.
    Retorna 0 de valor se exceder a capacidade.
    """
    peso_total = sum(p for i, p in enumerate(pesos) if solucao[i] == 1)
    valor_total = sum(v for i, v in enumerate(valores) if solucao[i] == 1)

    if peso_total > capacidade:
        return 0, peso_total
    return valor_total, peso_total


def gerar_solucao_inicial(tamanho: int) -> List[int]:
    """
    Gera uma solução inicial aleatória.
    """
    return [random.randint(0, 1) for _ in range(tamanho)]


def gerar_vizinho(solucao: List[int]) -> List[int]:
    """
    Gera uma solução vizinha trocando um bit aleatório.
    """
    vizinho = solucao[:]
    idx = random.randint(0, len(solucao) - 1)
    vizinho[idx] = 1 - vizinho[idx]
    return vizinho


def bee_algorithm(
    pesos: List[int],
    valores: List[int],
    capacidade: int,
    n_abelhas: int = 30,
    n_melhores: int = 10,
    n_vizinhos: int = 2,
    n_iter: int = 50
) -> Tuple[List[int], int, int]:
    """
    Executa o Bee Algorithm para o Problema da Mochila.
    Retorna a melhor solução, valor total e peso total.
    """
    n = len(pesos)
    melhores_solucoes = []

    for _ in range(n_iter):
        abelhas = [gerar_solucao_inicial(n) for _ in range(n_abelhas)]
        avaliacoes = [(sol, *avaliar_solucao(sol, pesos, valores, capacidade)) for sol in abelhas]
        avaliacoes.sort(key=lambda x: x[1], reverse=True)

        melhores = avaliacoes[:n_melhores]

        for sol, _, _ in melhores:
            vizinhos = [gerar_vizinho(sol) for _ in range(n_vizinhos)]
            vizinhos.append(sol)

            vizinhos_avaliados = [
                (v, *avaliar_solucao(v, pesos, valores, capacidade)) for v in vizinhos
            ]
            melhor_vizinho = max(vizinhos_avaliados, key=lambda x: x[1])
            melhores_solucoes.append(melhor_vizinho)

    melhor_global = max(melhores_solucoes, key=lambda x: x[1])
    return melhor_global[0], melhor_global[1], melhor_global[2]


def gerar_instancia_aleatoria(
    num_itens: int, max_peso: int = 10, max_valor: int = 50
) -> Tuple[List[int], List[int], int]:
    """
    Gera uma instância aleatória do problema da mochila.
    """
    pesos = [random.randint(1, max_peso) for _ in range(num_itens)]
    valores = [random.randint(1, max_valor) for _ in range(num_itens)]
    capacidade = random.randint(int(sum(pesos) * 0.3), int(sum(pesos) * 0.6))
    return pesos, valores, capacidade


def executar_testes_bee() -> List[dict]:
    """
    Executa testes com instâncias aleatórias e retorna os resultados.
    """
    resultados = []
    for n in [5, 1000, 10000]:
        pesos, valores, capacidade = gerar_instancia_aleatoria(n)
        inicio = time.time()
        solucao, valor, peso = bee_algorithm(pesos, valores, capacidade)
        fim = time.time()

        resultados.append({
            "algoritmo": "Bee Algorithm",
            "n_itens": n,
            "capacidade": capacidade,
            "valor_total": valor,
            "peso_total": peso,
            "tempo_execucao": round(fim - inicio, 5),
            "pesos": pesos,
            "valores": valores,
            "melhor_solucao": solucao
        })

    return resultados
