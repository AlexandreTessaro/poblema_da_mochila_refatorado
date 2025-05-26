import unittest
from algEnxParticulas import gerar_instancia_aleatoria, avaliar, Particula, pso, sigmoid

class TestPSOAlgorithm(unittest.TestCase):

    def test_gerar_instancia_aleatoria(self):
        pesos, valores, capacidade = gerar_instancia_aleatoria(10)
        self.assertEqual(len(pesos), 10)
        self.assertEqual(len(valores), 10)
        self.assertTrue(capacidade > 0)
        self.assertTrue(all(p > 0 for p in pesos))
        self.assertTrue(all(v > 0 for v in valores))

    def test_sigmoid(self):
        self.assertAlmostEqual(sigmoid(0), 0.5)
        self.assertGreater(sigmoid(1), 0.5)
        self.assertLess(sigmoid(-1), 0.5)

    def test_avaliar_valida_solucao_valida(self):
        pesos = [2, 3, 5]
        valores = [50, 60, 140]
        capacidade = 8
        solucao = [1, 0, 1]  # peso 7, valor 190
        valor, peso = avaliar(solucao, pesos, valores, capacidade)
        self.assertEqual(valor, 190)
        self.assertEqual(peso, 7)

    def test_avaliar_solucao_invalida(self):
        pesos = [2, 3, 5]
        valores = [50, 60, 140]
        capacidade = 7
        solucao = [1, 1, 1]  # peso 10, que é > capacidade
        valor, peso = avaliar(solucao, pesos, valores, capacidade)
        self.assertEqual(valor, 0)
        self.assertEqual(peso, 10)

    def test_particula_binarizacao(self):
        n_itens = 5
        pesos = [1]*n_itens
        valores = [1]*n_itens
        capacidade = 5
        particula = Particula(n_itens, pesos, valores, capacidade)
        bin_pos = particula.binarizar()
        self.assertEqual(len(bin_pos), n_itens)
        self.assertTrue(all(b in [0, 1] for b in bin_pos))

    def test_pso_retorna_solucao_valida(self):
        pesos = [2, 3, 4]
        valores = [50, 60, 70]
        capacidade = 5
        solucao, valor, peso = pso(pesos, valores, capacidade, n_particulas=10, n_iteracoes=20)
        self.assertEqual(len(solucao), len(pesos))
        self.assertTrue(all(bit in [0, 1] for bit in solucao))
        self.assertTrue(peso <= capacidade)
        self.assertTrue(valor >= 0)

if __name__ == "__main__":
    unittest.main()
