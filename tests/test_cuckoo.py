import unittest
from algCuckoo import (
    cuckoo_search,
    gerar_instancia_aleatoria,
    avaliar_solucao,
)


class TestCuckooSearch(unittest.TestCase):
    def setUp(self):
        self.n_itens = 50
        self.pesos, self.valores, self.capacidade = gerar_instancia_aleatoria(self.n_itens)

    def test_solucao_valida(self):
        solucao, valor_total, peso_total = cuckoo_search(
            self.pesos, self.valores, self.capacidade, n_ninhos=20, n_iteracoes=10
        )

        # A solução deve ter o mesmo tamanho da quantidade de itens
        self.assertEqual(len(solucao), self.n_itens)

        # Os valores dos itens devem ser 0 ou 1
        self.assertTrue(all(gene in [0, 1] for gene in solucao))

        # O valor total retornado deve ser igual ao valor calculado pela função de avaliação
        valor_avaliado, peso_avaliado = avaliar_solucao(solucao, self.pesos, self.valores, self.capacidade)
        self.assertEqual(valor_total, valor_avaliado)
        self.assertEqual(peso_total, peso_avaliado)

        # A solução não pode ultrapassar a capacidade
        self.assertLessEqual(peso_total, self.capacidade)


if __name__ == '__main__':
    unittest.main()
