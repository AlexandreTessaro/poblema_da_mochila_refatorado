import unittest
from refatorado.bio.algColonFormigas import (
    gerar_instancia_aleatoria,
    avaliar_solucao,
    construir_solucao,
    atualizar_feromonios,
    aco_knapsack
)


class TestACOAlgorithm(unittest.TestCase):

    def setUp(self):
        self.pesos = [2, 3, 4, 5]
        self.valores = [3, 4, 5, 6]
        self.capacidade = 5
        self.feromonio = [1.0 for _ in self.pesos]

    def test_avaliar_solucao_valida(self):
        solucao = [1, 0, 0, 0]  # Peso = 2, Valor = 3
        valor, peso = avaliar_solucao(solucao, self.pesos, self.valores, self.capacidade)
        self.assertEqual(valor, 3)
        self.assertEqual(peso, 2)

    def test_avaliar_solucao_invalida(self):
        solucao = [1, 1, 1, 1]  # Excede a capacidade
        valor, peso = avaliar_solucao(solucao, self.pesos, self.valores, self.capacidade)
        self.assertEqual(valor, 0)
        self.assertTrue(peso > self.capacidade)

    def test_construir_solucao_respeita_capacidade(self):
        solucao = construir_solucao(self.pesos, self.valores, self.capacidade, self.feromonio, 1.0, 2.0)
        _, peso_total = avaliar_solucao(solucao, self.pesos, self.valores, self.capacidade)
        self.assertLessEqual(peso_total, self.capacidade)

    def test_atualizar_feromonios_funciona(self):
        melhor_solucao = [1, 0, 1, 0]
        melhor_peso = 6
        feromonio_original = self.feromonio.copy()
        atualizar_feromonios(self.feromonio, melhor_solucao, melhor_peso, 0.1, 100)
        for i in range(len(self.feromonio)):
            self.assertNotEqual(self.feromonio[i], feromonio_original[i])

    def test_aco_knapsack_retorna_resultado(self):
        solucao, valor, peso = aco_knapsack(self.pesos, self.valores, self.capacidade, n_formigas=10, n_iteracoes=5)
        self.assertIsInstance(solucao, list)
        self.assertIsInstance(valor, int)
        self.assertIsInstance(peso, int)
        self.assertLessEqual(peso, self.capacidade)


if __name__ == "__main__":
    unittest.main()
