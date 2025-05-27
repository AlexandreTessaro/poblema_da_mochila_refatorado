import random
import time
import pandas as pd
from typing import List, Tuple


def gerar_instancia_aleatoria(
    n_itens: int, max_peso: int = 10, max_valor: int = 20
) -> Tuple[List[int], List[int], int]:
    pesos = [random.randint(1, max_peso) for _ in range(n_itens)]
    valores = [random.randint(1, max_valor) for _ in range(n_itens)]
    capacidade = random.randint(int(0.3 * sum(pesos)), int(0.6 * sum(pesos)))
    return pesos, valores, capacidade


def avaliar_solucao(
    solucao: List[int], pesos: List[int], valores: List[int], capacidade: int
) -> Tuple[int, int]:
    peso_total = sum(p * i for p, i in zip(pesos, solucao))
    valor_total = sum(v * i for v, i in zip(valores, solucao))
    if peso_total > capacidade:
        return 0, peso_total
    return valor_total, peso_total


def gerar_solucao_aleatoria(n: int) -> List[int]:
    return [random.randint(0, 1) for _ in range(n)]


def aplicar_levy_flight(solucao: List[int]) -> List[int]:
    nova_solucao = solucao[:]
    for i in range(len(nova_solucao)):
        if random.random() < 0.5:
            nova_solucao[i] = 1 - nova_solucao[i]
    return nova_solucao


def cuckoo_search(
    pesos: List[int],
    valores: List[int],
    capacidade: int,
    n_ninhos: int = 25,
    n_iteracoes: int = 50,
    taxa_abandono: float = 0.25,
) -> Tuple[List[int], int, int]:
    n = len(pesos)
    ninhos = [gerar_solucao_aleatoria(n) for _ in range(n_ninhos)]
    fitness = [avaliar_solucao(n, pesos, valores, capacidade)[0] for n in ninhos]
    melhor_ninho = ninhos[fitness.index(max(fitness))]

    for _ in range(n_iteracoes):
        for i in range(n_ninhos):
            novo_ninho = aplicar_levy_flight(ninhos[i])
            novo_fitness, _ = avaliar_solucao(novo_ninho, pesos, valores, capacidade)
            if novo_fitness > fitness[i]:
                ninhos[i] = novo_ninho
                fitness[i] = novo_fitness

        n_abandonados = int(taxa_abandono * n_ninhos)
        for _ in range(n_abandonados):
            idx = random.randint(0, n_ninhos - 1)
            ninhos[idx] = gerar_solucao_aleatoria(n)
            fitness[idx] = avaliar_solucao(ninhos[idx], pesos, valores, capacidade)[0]

        melhor_ninho = ninhos[fitness.index(max(fitness))]

    melhor_valor, melhor_peso = avaliar_solucao(melhor_ninho, pesos, valores, capacidade)
    return melhor_ninho, melhor_valor, melhor_peso


def main() -> pd.DataFrame:
    resultados = []
    for n_itens in [5, 1000, 10000]:
        pesos, valores, capacidade = gerar_instancia_aleatoria(n_itens)
        inicio = time.time()
        solucao, valor, peso = cuckoo_search(pesos, valores, capacidade)
        fim = time.time()

        resultados.append({
            "algoritmo": "Cuckoo Search",
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

def executar_testes_cuckoo():
    return main().to_dict(orient="records")


if __name__ == "__main__":
    df_resultado = main()
    print(df_resultado)
