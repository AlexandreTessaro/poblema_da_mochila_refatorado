import random
import time
import pandas as pd
from utils.geracao import gerar_instancia_aleatoria, gerar_solucao
from utils.avalicao import avaliar


N_ABELHAS = 30
N_MELHORES = 10
N_VIZINHOS = 2
N_ITERACOES = 50

def gerar_vizinho(solucao):
    """Gera um vizinho modificando 1 bit aleatoriamente."""
    vizinho = solucao[:]
    idx = random.randint(0, len(solucao) - 1)
    vizinho[idx] = 1 - vizinho[idx]
    return vizinho

def bee_algorithm(pesos, valores, capacidade,
                  n_abelhas=N_ABELHAS,
                  n_melhores=N_MELHORES,
                  n_vizinhos=N_VIZINHOS,
                  n_iter=N_ITERACOES):
    """
    Executa o algoritmo das abelhas (Bee Algorithm) para o problema da mochila binária.
    """
    n = len(pesos)
    melhores_solucoes = []

    for _ in range(n_iter):
        abelhas = [gerar_solucao(n) for _ in range(n_abelhas)]
        avaliacoes = [(sol, *avaliar(sol, pesos, valores, capacidade)) for sol in abelhas]
        avaliacoes.sort(key=lambda x: x[1], reverse=True)
        melhores = avaliacoes[:n_melhores]

        novas_solucoes = []
        for sol, _, _ in melhores:
            vizinhos = [gerar_vizinho(sol) for _ in range(n_vizinhos)]
            vizinhos.append(sol)
            viz_avaliadas = [(v, *avaliar(v, pesos, valores, capacidade)) for v in vizinhos]
            melhor_vizinho = max(viz_avaliadas, key=lambda x: x[1])
            novas_solucoes.append(melhor_vizinho)

        melhores_solucoes.extend(novas_solucoes)

    melhor_global = max(melhores_solucoes, key=lambda x: x[1])
    return melhor_global[0], melhor_global[1], melhor_global[2]

def executar_testes():
    """Executa o Bee Algorithm para diferentes tamanhos de instância e coleta métricas."""
    tamanhos = [5, 1000, 10000]
    resultados = []

    for n in tamanhos:
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

    return pd.DataFrame(resultados)

def main():
    df = executar_testes()
    print("\nResumo dos resultados:")
    print(df)
    return df

if __name__ == "__main__":
    main()
