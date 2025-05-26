# Relatório de Resultados: Algoritmos Bio-Inspirados

## Equipe:
* Gabriel D. Kasten
* Gustavo Henrique Costa
* Lucas Mendes Israel

## 1. Introdução

Este relatório apresenta os resultados obtidos com a aplicação de algoritmos bio-inspirados na resolução do Problema da Mochila 0/1, um problema clássico de otimização combinatória. Os algoritmos analisados foram:

## 2. Descrição do Funcionamento dos Algoritmos

### Bee Algorithm:
O Bee Algorithm é inspirado no comportamento de coleta das abelhas. As abelhas exploram a vizinhança de uma solução para encontrar o néctar mais eficiente. No contexto do Problema da Mochila, cada abelha tenta encontrar uma combinação de itens que maximiza o valor total sem ultrapassar a capacidade da mochila.

### Algoritmo ACO (Ant Colony Optimization):
O ACO é baseado no comportamento das formigas para encontrar o caminho mais curto até uma fonte de comida. As formigas deixam trilhas de feromônio para orientar outras formigas. No Problema da Mochila, cada formiga constrói uma solução (um subconjunto de itens), e a solução é aprimorada ao longo do tempo com base na quantidade de feromônio depositado.

### Cuckoo Search:
O Cuckoo Search é inspirado no comportamento dos cucos, que colocam seus ovos nos ninhos de outras aves. O algoritmo envolve a troca de soluções entre um grupo de "ninhos" e a substituição de soluções menos promissoras por novas soluções geradas aleatoriamente.

### PSO (Particle Swarm Optimization):
O PSO é baseado no comportamento coletivo de partículas que buscam encontrar o melhor caminho em um espaço de solução. Cada partícula ajusta sua posição e velocidade com base nas experiências passadas de si mesma e de suas vizinhas, buscando encontrar a melhor solução.

### Algoritmo Genético:
O Algoritmo Genético é inspirado na seleção natural e nos processos de evolução. Ele utiliza operadores como seleção, cruzamento e mutação para evoluir uma população de soluções até encontrar a melhor solução possível para o Problema da Mochila.

## 3. Resultados
A tabela abaixo mostra os tempos de execução de cada algoritmo para diferentes instâncias do Problema da Mochila, com base em diferentes valores de n_itens:

| Algoritmo        | n_itens | Bee Algorithm | Algoritmo ACO | Cuckoo Search | PSO       | Algoritmo Genético |
|------------------|---------|---------------|---------------|---------------|-----------|--------------------|
| **Instância 1**  | 5       | 0.00800       | 0.00457       | 0.00300       | 0.019850  | 0.00000            |
| **Instância 2**  | 1000    | 0.85355       | 0.95148       | 0.30831       | 2.913163  | 0.01201            |
| **Instância 3**  | 10000   | 8.23219       | 10.12230      | 3.09650       | 30.499538 | 0.11217            |

Complexidade Assintótica (Big O)

Algoritmo Genético (GA)

Complexidade: O(n * P * G), onde:

n é o número de itens (tamanho do espaço de solução).

P é o número de indivíduos na população (tamanho da população).

G é o número de gerações (quantas vezes o algoritmo executa iterações).

Explicação: A complexidade é dominada pelo número de gerações e pelo tamanho da população. A cada geração, a população inteira é avaliada, o que torna o GA mais custoso em termos de tempo de execução, principalmente para grandes n.

Algoritmo ACO (Ant Colony Optimization)
Complexidade: O(n * M * I), onde:

n é o número de itens.

M é o número de formigas.

I é o número de iterações.

Explicação: O ACO avalia múltiplas soluções para cada formiga em cada iteração, o que significa que o tempo de execução depende linearmente do número de formigas e iterações.

Cuckoo Search
Complexidade: O(n * N * I), onde:

n é o número de itens.

N é o número de ninhos.

I é o número de iterações.

Explicação: O Cuckoo Search tem uma estrutura relativamente simples. A atualização dos ninhos e a busca de soluções através de voo de Lévy são diretas, mas o número de iterações pode impactar o desempenho.

PSO (Particle Swarm Optimization)
Complexidade: O(n * P * I), onde:

n é o número de itens.

P é o número de partículas.

I é o número de iterações.

Explicação: Similar ao ACO, PSO também é dependente do número de partículas e iterações. Cada partícula atualiza sua posição e velocidade a cada iteração, tornando o algoritmo relativamente custoso em termos de tempo de execução.

Bee Algorithm
Complexidade: O(n * P * I), onde:

n é o número de itens.

P é o número de abelhas.

I é o número de iterações.

Explicação: O Bee Algorithm, apesar de eficiente para pequenas instâncias, também depende do número de abelhas e iterações. A atualização das posições das abelhas e a busca local para vizinhos tornam sua complexidade relativamente baixa.

### Observações:
Para instâncias menores (5 itens), o tempo de execução é muito rápido, com todos os algoritmos apresentando resultados em milissegundos.

Para instâncias maiores (1000 e 10000 itens), o desempenho de cada algoritmo varia significativamente. O Algoritmo Genético apresentou o melhor desempenho para n_itens = 5, mas à medida que o número de itens cresce, outros algoritmos como Bee Algorithm e Cuckoo Search mostraram melhor desempenho.

PSO foi o algoritmo com o tempo de execução mais longo nas instâncias maiores.

## 4. Exemplos de Entrada e Saída
Exemplo de Entrada:
Para a instância com 5 itens, temos os seguintes dados:

Pesos: [2, 3, 4, 5, 1]

Valores: [3, 4, 5, 6, 2]

Capacidade da mochila: 5

Exemplo de Saída:
A solução pode consistir em selecionar os itens 1, 3 e 5, resultando no seguinte:

Itens selecionados: [1, 0, 1, 0, 1]

Valor total: 3 + 5 + 2 = 10

Peso total: 2 + 4 + 1 = 7 (não ultrapassando a capacidade da mochila)

## 5. Dificuldades e Aprendizados

### Dificuldades:

#### Complexidade Computacional: 

À medida que o número de itens aumenta, a complexidade computacional dos algoritmos cresce significativamente, especialmente para o PSO e o Algoritmo Genético, que envolvem muitos cálculos e ajustes de parâmetros.

#### Parâmetros dos Algoritmos: 
Encontrar os valores ideais para os parâmetros de cada algoritmo (como taxas de mutação, coeficientes no PSO, etc.) foi um desafio. Ajustes inadequados podem levar a soluções subótimas ou tempos de execução muito elevados.

### Aprendizados:

#### Importância dos Parâmetros: 
O ajuste de parâmetros (como taxas de mutação no Algoritmo Genético ou coeficientes no PSO) teve um grande impacto no desempenho de cada algoritmo. A calibração precisa é essencial para garantir bons resultados.

#### Uso de Algoritmos Bio-Inspirados: 
Observamos que os algoritmos bio-inspirados podem ser muito eficientes para resolver problemas de otimização, mas a escolha do algoritmo depende muito do tamanho da instância do problema.

#### Experimentação e Ajustes: 
O processo de experimentação e ajustes finos foi fundamental para alcançar os melhores resultados, e o uso de diferentes algoritmos ajudou a comparar os pontos fortes e fracos de cada abordagem.

## 6. Conclusão
Este estudo comparou o desempenho de diferentes algoritmos bio-inspirados na solução do Problema da Mochila. Observamos que, enquanto algoritmos como o Bee Algorithm e o Cuckoo Search apresentaram melhor desempenho em instâncias maiores, o PSO e o Algoritmo Genético foram mais eficientes para instâncias menores.

Os resultados destacam a importância de escolher o algoritmo certo com base no tamanho e na natureza do problema, e o impacto que parâmetros mal ajustados podem ter na eficiência dos algoritmos. A experimentação foi essencial para encontrar a solução ótima.

