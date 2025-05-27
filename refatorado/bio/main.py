import pandas as pd
import algBeeAlgorithm
import algColonFormigas
import algCuckoo
import algEnxParticulas
import algGeneticos

# Dicionário dos módulos dos algoritmos
algoritmos = {
    "Bee Algorithm": algBeeAlgorithm,
    "Algoritmo ACO": algColonFormigas,
    "Cuckoo Search": algCuckoo,
    "PSO": algEnxParticulas,
    "Algoritmo Genético": algGeneticos,
}

# Mapeamento das funções de teste para cada algoritmo
funcoes_teste = {
    "Bee Algorithm": "executar_testes_bee",
    "Algoritmo ACO": "executar_testes_aco",
    "Cuckoo Search": "executar_testes_cuckoo",
    "PSO": "executar_testes_algEnxParticulas",
    "Algoritmo Genético": "executar_testes_genetico",
}

resultados = []

for nome, modulo in algoritmos.items():
    print(f"Executando testes para: {nome}")
    
    func_nome = funcoes_teste.get(nome)
    
    if not func_nome:
        print(f"Nenhuma função de teste mapeada para {nome}")
        continue
    
    if not hasattr(modulo, func_nome):
        print(f"Função '{func_nome}' não encontrada no módulo do {nome}")
        continue
    
    try:
        func = getattr(modulo, func_nome)
        df = pd.DataFrame(func())
        df['algoritmo'] = nome
        resultados.append(df)
    except Exception as e:
        print(f"Erro ao executar {nome}: {e}")

# Concatenar resultados em um único DataFrame
if resultados:
    df_tempos = pd.concat(resultados, axis=0)

    # Selecionar colunas importantes (garantindo que existam)
    colunas_esperadas = ['n_itens', 'tempo_execucao', 'algoritmo']
    colunas_validas = [col for col in colunas_esperadas if col in df_tempos.columns]
    df_tempos = df_tempos[colunas_validas].copy()

    # Pivotar para formato de comparação lado a lado
    df_tempos_pivot = df_tempos.pivot(index='n_itens', columns='algoritmo', values='tempo_execucao').reset_index()

    # Garantir ordem das colunas no resultado
    ordem_colunas = ['n_itens'] + list(algoritmos.keys())
    colunas_finais = [col for col in ordem_colunas if col in df_tempos_pivot.columns]
    df_tempos_pivot = df_tempos_pivot[colunas_finais]

    print("\n=== Tabela de Tempos de Execução dos Algoritmos ===")
    print(df_tempos_pivot)

    # Opcional: salvar resultado para análise futura
    df_tempos_pivot.to_csv("tempos_algoritmos.csv", index=False)
    print("\nArquivo 'tempos_algoritmos.csv' salvo com os resultados.")
else:
    print("Nenhum resultado válido foi obtido.")
