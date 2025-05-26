import pandas as pd
import algBeeAlgorithm
import algColonFormigas
import algCuckoo
import algEnxParticulas
import algGeneticos

algoritmos = {
    "Bee Algorithm": algBeeAlgorithm,
    "Algoritmo ACO": algColonFormigas,
    "Cuckoo Search": algCuckoo,
    "PSO": algEnxParticulas,
    "Algoritmo Genético": algGeneticos,
}

resultados = []
for nome, modulo in algoritmos.items():
    # Ajuste para chamar a função correta que retorna a lista de resultados
    if hasattr(modulo, 'executar_testes_bee'):
        df = pd.DataFrame(modulo.executar_testes_bee())
    elif hasattr(modulo, 'executar_testes_aco'):
        df = pd.DataFrame(modulo.executar_testes_aco())
    elif hasattr(modulo, 'executar_testes_cuckoo'):
        df = pd.DataFrame(modulo.executar_testes_cuckoo())
    elif hasattr(modulo, 'executar_testes_pso'):
        df = pd.DataFrame(modulo.executar_testes_pso())
    elif hasattr(modulo, 'executar_testes_geneticos'):
        df = pd.DataFrame(modulo.executar_testes_geneticos())
    else:
        # Caso não ache função padrão, pode pular ou lançar erro
        continue
    
    resultados.append(df)

df_tempos = pd.concat(resultados, axis=0)

df_tempos = df_tempos[['n_itens', 'tempo_execucao', 'algoritmo']].copy()

df_tempos_pivot = df_tempos.pivot(index='n_itens', columns='algoritmo', values='tempo_execucao').reset_index()

ordem_colunas = ['n_itens'] + list(algoritmos.keys())
df_tempos_pivot = df_tempos_pivot[ordem_colunas]

print(df_tempos_pivot)
