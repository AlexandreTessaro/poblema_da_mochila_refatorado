import random
import math
import time
import pandas as pd

def gerar_instancia_aleatoria(n_itens, max_peso=10, max_valor=10):
    """
    Gera pesos, valores e capacidade aleatória para o problema da mochila.
    """
    pesos = [random.randint(1, max_peso) for _ in range(n_itens)]
    valores = [random.randint(1, max_valor) for _ in range(n_itens)]
    capacidade = int(0.2 * sum(pesos))
    return pesos, valores, capacidade

def sigmoid(x):
    """
    Função sigmoid para converter valores contínuos em probabilidades.
    """
    return 1 / (1 + math.exp(-x))

def avaliar(solucao_binaria, pesos, valores, capacidade):
    """
    Avalia a solução da mochila: retorna valor total se peso <= capacidade, senão 0.
    """
    peso_total = sum(p * i for p, i in zip(pesos, solucao_binaria))
    valor_total = sum(v * i for v, i in zip(valores, solucao_binaria))
    if peso_total > capacidade:
        return 0, peso_total
    return valor_total, peso_total

class Particula:
    def __init__(self, n_itens, pesos, valores, capacidade):
        self.n_itens = n_itens
        self.pesos = pesos
        self.valores = valores
        self.capacidade = capacidade
        self.posicao = [random.uniform(-4, -2) for _ in range(n_itens)]
        self.velocidade = [random.uniform(-1, 1) for _ in range(n_itens)]
        self.best_posicao = self.posicao[:]
        self.best_valor, _ = avaliar(self.binarizar(), pesos, valores, capacidade)

    def binarizar(self):
        return [1 if sigmoid(x) >= 0.5 else 0 for x in self.posicao]

    def atualizar_velocidade(self, global_best, c1=1.5, c2=1.5, w=0.8, limite_velocidade=4):
        for i in range(len(self.posicao)):
            r1 = random.random()
            r2 = random.random()
            cog = c1 * r1 * (self.best_posicao[i] - self.posicao[i])
            soc = c2 * r2 * (global_best[i] - self.posicao[i])
            nova_vel = w * self.velocidade[i] + cog + soc
            nova_vel = max(min(nova_vel, limite_velocidade), -limite_velocidade)
            self.velocidade[i] = nova_vel

    def atualizar_posicao(self):
        for i in range(len(self.posicao)):
            self.posicao[i] += self.velocidade[i]

    def atualizar_pessoal(self):
        bin_pos = self.binarizar()
        valor, _ = avaliar(bin_pos, self.pesos, self.valores, self.capacidade)
        if valor > self.best_valor:
            self.best_valor = valor
            self.best_posicao = self.posicao[:]

def pso(pesos, valores, capacidade, n_particulas=30, n_iteracoes=100):
    n_itens = len(pesos)
    enxame = [Particula(n_itens, pesos, valores, capacidade) for _ in range(n_particulas)]

    global_best = enxame[0].posicao[:]
    global_best_valor, _ = avaliar(enxame[0].binarizar(), pesos, valores, capacidade)

    for _ in range(n_iteracoes):
        for particula in enxame:
            particula.atualizar_velocidade(global_best)
            particula.atualizar_posicao()
            particula.atualizar_pessoal()

            valor, _ = avaliar(particula.binarizar(), pesos, valores, capacidade)
            if valor > global_best_valor:
                global_best = particula.posicao[:]
                global_best_valor = valor

    melhor_solucao = [1 if sigmoid(x) >= 0.5 else 0 for x in global_best]
    peso_total = sum(p * i for p, i in zip(pesos, melhor_solucao))
    return melhor_solucao, global_best_valor, peso_total

def main():
    tamanhos = [5, 1000, 10000]
    resultados = []

    for n_itens in tamanhos:
        pesos, valores, capacidade = gerar_instancia_aleatoria(n_itens)

        inicio = time.time()
        solucao, valor, peso = pso(pesos, valores, capacidade)
        fim = time.time()

        resultados.append({
            "algoritmo": "PSO",
            "n_itens": n_itens,
            "capacidade": capacidade,
            "valor_total": valor,
            "peso_total": peso,
            "tempo_execucao": round(fim - inicio, 5),
            "pesos": pesos,
            "valores": valores,
            "melhor_solucao": solucao
        })

    df_resultados = pd.DataFrame(resultados)
    return df_resultados

if __name__ == "__main__":
    df_resultados = main()
    print("\nResumo dos resultados de todos os testes:")
    print(df_resultados)
