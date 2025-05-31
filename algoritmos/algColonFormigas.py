import random
import time
import pandas as pd

from utils.geracao import gerar_instancia_aleatoria
from utils.avalicao import avaliar

FORMIGAS_PADRAO = 50
ITERACOES_PADRAO = 50
ALFA_PADRAO = 1.0
BETA_PADRAO = 2.0
RHO_PADRAO = 0.1
Q_PADRAO = 100

def aco_knapsack(
    pesos,
    valores,
    capacidade,
    n_formigas=FORMIGAS_PADRAO,
    n_iteracoes=ITERACOES_PADRAO,
    alfa=ALFA_PADRAO,
    beta=BETA_PADRAO,
    rho=RHO_PADRAO,
    Q=Q_PADRAO
):
    """Executa o algoritmo ACO para resolver o problema da mochila binária."""
    n = len(pesos)
    feromonio = [1.0] * n
    melhor_solucao = None
    melhor_valor = 0
    melhor_peso = 0

    for _ in range(n_iteracoes):
        for _ in range(n_formigas):
            solucao = construir_solucao(pesos, valores, capacidade, feromonio, alfa, beta)
            valor, peso = avaliar(solucao, pesos, valores, capacidade)
            if valor > melhor_valor:
                melhor_solucao = solucao
                melhor_valor = valor
                melhor_peso = peso

        atualizar_feromonio(feromonio, melhor_solucao, melhor_peso, rho, Q)

    return melhor_solucao, melhor_valor, melhor_peso

def construir_solucao(pesos, valores, capacidade, feromonio, alfa, beta):
    """Constrói uma solução probabilística com base em feromônio e atratividade."""
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

def atualizar_feromonio(feromonio, melhor_solucao, melhor_peso, rho, Q):
    """Atualiza a trilha de feromônio baseada na melhor solução."""
    for i in range(len(feromonio)):
        feromonio[i] *= (1 - rho)
        if melhor_solucao and melhor_solucao[i] == 1:
            feromonio[i] += Q / (1 + melhor_peso)

def executar_testes():
    """Executa o algoritmo para diferentes tamanhos de instância e coleta os resultados."""
    tamanhos = [5, 1000, 10000]
    resultados = []

    for n_itens in tamanhos:
        pesos, valores, capacidade = gerar_instancia_aleatoria(n_itens)
        inicio = time.time()
        solucao, valor, peso = aco_knapsack(pesos, valores, capacidade)
        fim = time.time()

        resultados.append({
            "algoritmo": "Algoritmo ACO",
            "n_itens": n_itens,
            "capacidade": capacidade,
            "valor_total": valor,
            "peso_total": peso,
            "tempo_execucao": round(fim - inicio, 5),
            "pesos": pesos,
            "valores": valores,
            "melhor_solucao": solucao
        })

    return pd.DataFrame(resultados)

def main():
    df = executar_testes()
    print("\nResumo dos resultados:")
    print(df)
    return df

if __name__ == "__main__":
    main()
