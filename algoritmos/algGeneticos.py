import random
import time
import pandas as pd

from utils.geracao import gerar_instancia_aleatoria
from utils.avalicao import avaliar


def gerar_individuo(n_itens):
    return [random.randint(0, 1) for _ in range(n_itens)]


def avaliar_individuo(individuo, pesos, valores, capacidade):
    peso_total = sum(p * i for p, i in zip(pesos, individuo))
    valor_total = sum(v * i for v, i in zip(valores, individuo))
    if peso_total > capacidade:
        excesso = peso_total - capacidade
        return valor_total - excesso * 2
    return valor_total


def selecao(populacao, pesos, valores, capacidade):
    torneio = random.sample(populacao, 3)
    torneio.sort(key=lambda ind: avaliar_individuo(ind, pesos, valores, capacidade), reverse=True)
    return torneio[0], torneio[1]


def crossover(pai1, pai2):
    ponto = random.randint(1, len(pai1) - 1)
    return pai1[:ponto] + pai2[ponto:], pai2[:ponto] + pai1[ponto:]


def mutacao(individuo, taxa_mutacao):
    return [1 - gene if random.random() < taxa_mutacao else gene for gene in individuo]


def algoritmo_genetico(pesos, valores, capacidade, tam_populacao=20, taxa_mutacao=0.1, n_geracoes=50):
    n_itens = len(pesos)
    populacao = [gerar_individuo(n_itens) for _ in range(tam_populacao)]
    melhor_solucao = None
    melhor_valor = float('-inf')

    for _ in range(n_geracoes):
        nova_populacao = []
        for _ in range(tam_populacao // 2):
            pai1, pai2 = selecao(populacao, pesos, valores, capacidade)
            filho1, filho2 = crossover(pai1, pai2)
            nova_populacao.extend([mutacao(filho1, taxa_mutacao), mutacao(filho2, taxa_mutacao)])
        populacao = nova_populacao

        for individuo in populacao:
            valor = avaliar_individuo(individuo, pesos, valores, capacidade)
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_solucao = individuo

    peso_total = sum(p * i for p, i in zip(pesos, melhor_solucao))
    return melhor_solucao, melhor_valor, peso_total


def executar_testes():
    tamanhos = [5, 1000, 10000]
    resultados = []

    for n in tamanhos:
        pesos, valores, capacidade = gerar_instancia_aleatoria(n)
        inicio = time.time()
        solucao, valor, peso_total = algoritmo_genetico(pesos, valores, capacidade)
        fim = time.time()

        resultados.append({
            "algoritmo": "Algoritmo Genético",
            "n_itens": n,
            "capacidade": capacidade,
            "valor_total": valor,
            "peso_total": peso_total,
            "tempo_execucao": round(fim - inicio, 5),
            "pesos": pesos,
            "valores": valores,
            "melhor_solucao": solucao
        })

    return pd.DataFrame(resultados)


def main():
    df = executar_testes()
    print(df)
    return df


if __name__ == "__main__":
    main()
