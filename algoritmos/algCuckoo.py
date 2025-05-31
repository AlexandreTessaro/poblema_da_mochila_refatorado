import random
import time
import pandas as pd

from utils.avalicao import avaliar
from utils.geracao import gerar_solucao, gerar_instancia_aleatoria

DEFAULT_NINHOS = 25
DEFAULT_ITERACOES = 50
TAXA_ABANDONO = 0.25

def levy_flight(solucao):
    """Realiza a perturbação estilo Levy Flight (flip binário com probabilidade)."""
    return [1 - bit if random.random() < 0.5 else bit for bit in solucao]

def cuckoo_search(pesos, valores, capacidade, n_ninhos=DEFAULT_NINHOS, n_iteracoes=DEFAULT_ITERACOES, pa=TAXA_ABANDONO):
    """Executa o algoritmo Cuckoo Search para o problema da mochila binária."""
    n = len(pesos)
    ninhos = [gerar_solucao(n) for _ in range(n_ninhos)]
    fitness = [avaliar(ninho, pesos, valores, capacidade)[0] for ninho in ninhos]
    melhor_ninho = ninhos[fitness.index(max(fitness))]

    for _ in range(n_iteracoes):
        for i in range(n_ninhos):
            novo_ninho = levy_flight(ninhos[i])
            novo_fitness, _ = avaliar(novo_ninho, pesos, valores, capacidade)
            if novo_fitness > fitness[i]:
                ninhos[i] = novo_ninho
                fitness[i] = novo_fitness

        n_abandonados = int(pa * n_ninhos)
        for _ in range(n_abandonados):
            idx = random.randint(0, n_ninhos - 1)
            ninhos[idx] = gerar_solucao(n)
            fitness[idx] = avaliar(ninhos[idx], pesos, valores, capacidade)[0]

        melhor_ninho = ninhos[fitness.index(max(fitness))]

    melhor_valor, melhor_peso = avaliar(melhor_ninho, pesos, valores, capacidade)
    return melhor_ninho, melhor_valor, melhor_peso

def executar_testes():
    """Executa testes com diferentes tamanhos de instâncias e coleta os resultados."""
    tamanhos = [5, 1000, 10000]
    resultados = []

    for n in tamanhos:
        pesos, valores, capacidade = gerar_instancia_aleatoria(n)
        inicio = time.time()
        solucao, valor, peso = cuckoo_search(pesos, valores, capacidade)
        fim = time.time()

        resultados.append({
            "algoritmo": "Cuckoo Search",
            "n_itens": n,
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
