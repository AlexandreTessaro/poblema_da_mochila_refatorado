def avaliar(solucao, pesos, valores, capacidade):
    peso_total = sum(p * i for p, i in zip(pesos, solucao))
    valor_total = sum(v * i for v, i in zip(valores, solucao))
    return (valor_total, peso_total) if peso_total <= capacidade else (0, peso_total)
