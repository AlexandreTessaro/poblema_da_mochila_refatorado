import random
import math
import time
import pandas as pd

from utils.geracao import gerar_instancia_aleatoria
from utils.avalicao import avaliar

N_PARTICULAS = 30
N_ITERACOES = 100
COEF_COGNITIVO = 1.5
COEF_SOCIAL = 1.5
INERCIA = 0.8
LIMITE_VELOCIDADE = 4

def sigmoid(x):
    """Função sigmoide para binarização da posição."""
    return 1 / (1 + math.exp(-x))

class Particula:
    def __init__(self, n_itens, pesos, valores, capacidade):
        self.n_itens = n_itens
        self.pesos = pesos
        self.valores = valores
        self.capacidade = capacidade

        self.posicao = [random.uniform(-4, -2) for _ in range(n_itens)]
        self.velocidade = [random.uniform(-1, 1) for _ in range(n_itens)]
        self.best_posicao = self.posicao[:]
        self.best_valor = avaliar(self.binarizar(), pesos, valores, capacidade)[0]

    def binarizar(self):
        """Converte posição contínua para binária."""
        return [1 if sigmoid(x) >= 0.5 else 0 for x in self.posicao]

    def atualizar_velocidade(self, global_best):
        """Atualiza a velocidade com base em inércia, cognição e social."""
        for i in range(self.n_itens):
            r1, r2 = random.random(), random.random()
            cog = COEF_COGNITIVO * r1 * (self.best_posicao[i] - self.posicao[i])
            soc = COEF_SOCIAL * r2 * (global_best[i] - self.posicao[i])
            nova_vel = INERCIA * self.velocidade[i] + cog + soc
            self.velocidade[i] = max(min(nova_vel, LIMITE_VELOCIDADE), -LIMITE_VELOCIDADE)

    def atualizar_posicao(self):
        """Atualiza a posição da partícula com base na velocidade."""
        for i in range(self.n_itens):
            self.posicao[i] += self.velocidade[i]

    def atualizar_best_pessoal(self):
        """Atualiza a melhor posição pessoal da partícula."""
        valor = avaliar(self.binarizar(), self.pesos, self.valores, self.capacidade)[0]
        if valor > self.best_valor:
            self.best_valor = valor
            self.best_posicao = self.posicao[:]

def pso(n_itens, pesos, valores, capacidade):
    """Executa o algoritmo PSO para o problema da mochila binária."""
    enxame = [Particula(n_itens, pesos, valores, capacidade) for _ in range(N_PARTICULAS)]
    global_best = enxame[0].posicao[:]
    global_best_valor = avaliar(enxame[0].binarizar(), pesos, valores, capacidade)[0]

    for _ in range(N_ITERACOES):
        for particula in enxame:
            particula.atualizar_velocidade(global_best)
            particula.atualizar_posicao()
            particula.atualizar_best_pessoal()

            valor = avaliar(particula.binarizar(), pesos, valores, capacidade)[0]
            if valor > global_best_valor:
                global_best = particula.posicao[:]
                global_best_valor = valor

    melhor_solucao = [1 if sigmoid(x) >= 0.5 else 0 for x in global_best]
    peso_total = sum(p * i for p, i in zip(pesos, melhor_solucao))
    return melhor_solucao, global_best_valor, peso_total

def executar_testes():
    """Executa o PSO para diferentes tamanhos de instância e coleta métricas."""
    tamanhos = [5, 1000, 10000]
    resultados = []

    for n_itens in tamanhos:
        pesos, valores, capacidade = gerar_instancia_aleatoria(n_itens)

        inicio = time.time()
        solucao, valor, peso_total = pso(n_itens, pesos, valores, capacidade)
        fim = time.time()

        resultados.append({
            "algoritmo": "PSO",
            "n_itens": n_itens,
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
    print("\nResumo dos resultados de todos os testes:")
    print(df)
    return df

if __name__ == "__main__":
    main()
