import unittest
import algGeneticos  # Supondo que seu arquivo refatorado esteja salvo como algGeneticos.py

class TestAlgoritmoGenetico(unittest.TestCase):
    def setUp(self):
        # Gerar uma instância pequena para testes
        self.pesos = [2, 3, 4, 5]
        self.valores = [3, 4, 5, 6]
        self.capacidade = 5

    def test_gerar_individuo(self):
        individuo = algGeneticos.gerar_individuo(len(self.pesos))
        self.assertEqual(len(individuo), len(self.pesos))
        self.assertTrue(all(gene in [0,1] for gene in individuo))

    def test_avaliar_individuo(self):
        individuo = [1, 0, 1, 0]
        valor = algGeneticos.avaliar_individuo(individuo, self.pesos, self.valores, self.capacidade)
        self.assertIsInstance(valor, (int, float))
        # Peso total = 2 + 4 = 6 > capacidade(5), então valor deve conter penalidade
        self.assertLess(valor, 3 + 5)  # valor_total sem penalidade seria 8

    def test_crossover(self):
        pai1 = [1, 1, 0, 0]
        pai2 = [0, 0, 1, 1]
        filho1, filho2 = algGeneticos.crossover(pai1, pai2)
        self.assertEqual(len(filho1), len(pai1))
        self.assertEqual(len(filho2), len(pai2))
        self.assertTrue(all(gene in [0,1] for gene in filho1))
        self.assertTrue(all(gene in [0,1] for gene in filho2))

    def test_mutacao(self):
        individuo = [0, 0, 0, 0]
        mutado = algGeneticos.mutacao(individuo[:], 1.0)  # taxa_mutacao=1 garante mutação total
        self.assertNotEqual(individuo, mutado)

    def test_algoritmo_genetico(self):
        solucao, valor = algGeneticos.algoritmo_genetico(self.pesos, self.valores, self.capacidade,
                                                         tam_populacao=10, taxa_mutacao=0.1, n_geracoes=10)
        self.assertEqual(len(solucao), len(self.pesos))
        self.assertTrue(all(gene in [0,1] for gene in solucao))
        self.assertIsInstance(valor, (int, float))

if __name__ == '__main__':
    unittest.main()
