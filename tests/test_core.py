import unittest
from core import processar_pedido, finalizar_pedido
from estoque import cadastrar_produto, estoque

class TestGerenciamentoPedidos(unittest.TestCase):
    def setUp(self):
        estoque.clear()
        estoque["produto_teste"] = 5

    def test_cadastrar_produto_sucesso(self):
        resultado = cadastrar_produto("produto_teste", 10)
        self.assertTrue(resultado)
        self.assertEqual(estoque["produto_teste"], 15)

    def test_cadastrar_produto_negativo(self):
        resultado = cadastrar_produto("produto_teste", -5)
        self.assertFalse(resultado)

    def test_processar_pedido_sucesso(self):
        total = processar_pedido("produto_teste", 2, 10.0)
        self.assertEqual(total, 20.0)

    def test_processar_pedido_sem_estoque(self):
        with self.assertRaises(RuntimeError):
            processar_pedido("produto_teste", 10, 10.0)

    def test_finalizar_pedido_sucesso(self):
        sucesso = finalizar_pedido("produto_teste", 2)
        self.assertTrue(sucesso)
        self.assertEqual(estoque["produto_teste"], 3)

    def test_finalizar_pedido_sem_estoque(self):
        sucesso = finalizar_pedido("produto_teste", 10)
        self.assertFalse(sucesso)

if __name__ == "__main__":
    unittest.main()
