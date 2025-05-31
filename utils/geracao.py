import random

def gerar_instancia_aleatoria(n_itens, max_peso=10, max_valor=20):
    pesos = [random.randint(1, max_peso) for _ in range(n_itens)]
    valores = [random.randint(1, max_valor) for _ in range(n_itens)]
    capacidade = random.randint(int(0.3 * sum(pesos)), int(0.6 * sum(pesos)))
    return pesos, valores, capacidade

def gerar_solucao(n):
    return [random.randint(0, 1) for _ in range(n)]
