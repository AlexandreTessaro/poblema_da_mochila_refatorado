import time
import pandas as pd
import random
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "algoritmos"))

from algoritmos.algBeeAlgorithm import bee_algorithm
from algoritmos.algGeneticos import algoritmo_genetico
from algoritmos.algCuckoo import cuckoo_search
from algoritmos.algEnxParticulas import pso
from algoritmos.algColonFormigas import aco_knapsack

# Tamanhos de instâncias
tamanhos = [5, 1000, 10000]

algoritmos = [
    ("Bee Algorithm", bee_algorithm),
    ("Algoritmo ACO", aco_knapsack),
    ("Cuckoo Search", cuckoo_search),
    ("PSO", pso),
    ("Algoritmo Genético", algoritmo_genetico)
]

def gerar_instancia_aleatoria(n_itens):
    pesos = [random.randint(1, 100) for _ in range(n_itens)]
    valores = [random.randint(1, 100) for _ in range(n_itens)]
    capacidade = int(sum(pesos) * 0.5)
    return pesos, valores, capacidade

def executar_algoritmos():
    resultados = []

    for n_itens in tamanhos:
        pesos, valores, capacidade = gerar_instancia_aleatoria(n_itens)

        for nome, funcao in algoritmos:
            inicio = time.time()

            # Chamada específica para PSO
            if nome == "PSO":
                resultado = funcao(n_itens, pesos, valores, capacidade)
            else:
                resultado = funcao(pesos, valores, capacidade)

            fim = time.time()

            # Verifica se o algoritmo retornou 2 ou 3 elementos
            if len(resultado) == 2:
                solucao, valor = resultado
                peso = sum(p * i for p, i in zip(pesos, solucao))
            else:
                solucao, valor, peso = resultado

            resultados.append({
                "algoritmo": nome,
                "n_itens": n_itens,
                "capacidade": capacidade,
                "valor_total": valor,
                "peso_total": peso,
                "tempo_execucao": round(fim - inicio, 5)
            })

    return pd.DataFrame(resultados)

def main():
    df_resultados = executar_algoritmos()
    print("\n📊 Resultados comparativos entre algoritmos:\n")
    print(df_resultados)
    df_resultados.to_csv("resultados_comparacao.csv", index=False)

if __name__ == "__main__":
    main()
