from logger import logger

estoque = {
    "produto_1": 10,
    "produto_2": 0,   # Sem estoque
}

def verificar_estoque(produto_id, quantidade):
    return estoque.get(produto_id, 0) >= quantidade

def cadastrar_produto(produto_id, quantidade):
    try:
        if quantidade < 0:
            logger.error("Quantidade negativa ao tentar cadastrar produto.")
            raise ValueError("Quantidade não pode ser negativa.")
        
        estoque[produto_id] = estoque.get(produto_id, 0) + quantidade
        logger.info(f"Produto '{produto_id}' cadastrado/atualizado com sucesso. Estoque: {estoque[produto_id]}")
        return True
    except Exception as e:
        logger.error(f"Erro ao cadastrar produto: {e}")
        return False
