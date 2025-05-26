import random
import time
from typing import List, Tuple
import pandas as pd


def gerar_instancia_aleatoria(n_itens: int, max_peso: int = 10, max_valor: int = 20) -> Tuple[List[int], List[int], int]:
    """
    Gera uma instância aleatória do problema da mochila.

    Retorna:
        pesos: lista de pesos dos itens
        valores: lista de valores dos itens
        capacidade: capacidade da mochila
    """
    pesos = [random.randint(1, max_peso) for _ in range(n_itens)]
    valores = [random.randint(1, max_valor) for _ in range(n_itens)]
    capacidade = random.randint(int(0.3 * sum(pesos)), int(0.6 * sum(pesos)))
    return pesos, valores, capacidade


def avaliar_solucao(solucao: List[int], pesos: List[int], valores: List[int], capacidade: int) -> Tuple[int, int]:
    """
    Avalia a solução retornando o valor total e o peso.

    Se ultrapassar a capacidade, o valor total é 0.
    """
    peso_total = sum(p * s for p, s in zip(pesos, solucao))
    valor_total = sum(v * s for v, s in zip(valores, solucao))
    if peso_total > capacidade:
        return 0, peso_total
    return valor_total, peso_total


def construir_solucao(
    pesos: List[int],
    valores: List[int],
    capacidade: int,
    feromonio: List[float],
    alfa: float,
    beta: float
) -> List[int]:
    """
    Constrói uma solução com base em feromônios e atratividade.
    """
    n = len(pesos)
    solucao = [0] * n
    peso_total = 0

    for i in range(n):
        if peso_total + pesos[i] <= capacidade:
            atratividade = (valores[i] / pesos[i]) if pesos[i] > 0 else 0
            prob = (feromonio[i] ** alfa) * (atratividade ** beta)
            if random.random() < prob / (1 + prob):
                solucao[i] = 1
                peso_total += pesos[i]

    return solucao


def atualizar_feromonios(
    feromonio: List[float],
    melhor_solucao: List[int],
    melhor_peso: int,
    rho: float,
    Q: int
) -> None:
    """
    Atualiza os níveis de feromônio com base na melhor solução.
    """
    for i in range(len(feromonio)):
        feromonio[i] *= (1 - rho)
        if melhor_solucao[i] == 1:
            feromonio[i] += Q / (1 + melhor_peso)


def aco_knapsack(
    pesos: List[int],
    valores: List[int],
    capacidade: int,
    n_formigas: int = 50,
    n_iteracoes: int = 50,
    alfa: float = 1.0,
    beta: float = 2.0,
    rho: float = 0.1,
    Q: int = 100
) -> Tuple[List[int], int, int]:
    """
    Algoritmo Otimização por Colônia de Formigas (ACO) para o Problema da Mochila.
    """
    n = len(pesos)
    feromonio = [1.0] * n
    melhor_solucao = [0] * n
    melhor_valor = 0
    melhor_peso = 0

    for _ in range(n_iteracoes):
        for _ in range(n_formigas):
            solucao = construir_solucao(pesos, valores, capacidade, feromonio, alfa, beta)
            valor, peso = avaliar_solucao(solucao, pesos, valores, capacidade)
            if valor > melhor_valor:
                melhor_solucao = solucao
                melhor_valor = valor
                melhor_peso = peso

        atualizar_feromonios(feromonio, melhor_solucao, melhor_peso, rho, Q)

    return melhor_solucao, melhor_valor, melhor_peso


def rodar_experimentos() -> pd.DataFrame:
    """
    Executa o algoritmo ACO para diferentes tamanhos de instâncias.
    Retorna um DataFrame com os resultados.
    """
    testes = []
    for n_itens in [5, 1000, 10000]:
        pesos, valores, capacidade = gerar_instancia_aleatoria(n_itens)
        inicio = time.time()
        solucao, valor, peso = aco_knapsack(pesos, valores, capacidade)
        fim = time.time()

        testes.append({
            "algoritmo": "ACO (Formigas)",
            "n_itens": n_itens,
            "capacidade": capacidade,
            "valor_total": valor,
            "peso_total": peso,
            "tempo_execucao": round(fim - inicio, 5),
            "pesos": pesos,
            "valores": valores,
            "melhor_solucao": solucao
        })

    return pd.DataFrame(testes)


if __name__ == "__main__":
    df_resultados = rodar_experimentos()
    print(df_resultados)
