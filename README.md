Algoritmos de Ordenação

Este repositório apresenta os principais algoritmos de ordenação, suas características, funcionamento e melhores usos. É ideal comparação e escolha do algoritmo mais adequado para cada situação.

1.Selection Sort (Ordenação por Seleção)

Como funciona:

O Selection Sort percorre a lista procurando o menor elemento e o coloca na primeira posição. Em seguida, procura o menor elemento restante e o coloca na segunda posição, repetindo até que todos os elementos estejam ordenados. Ordenação in-place (não usa memória extra significativa).
Vantagens:

Fácil de entender e implementar.
Poucas trocas (trocas de posição entre elementos).
Funciona bem para listas pequenas.

Desvantagens:

Lento para listas grandes.
Não é estável (pode mudar a ordem relativa de elementos iguais durante a ordenação).
Não se beneficia de listas parcialmente ordenadas.
Uso ideal: Pequenas listas ou quando a memória extra é limitada.

2.Bubble Sort

Como funciona:

Compara elementos vizinhos e troca-os se estiverem fora de ordem. Os elementos maiores vão para o final. Pode ser otimizado com flag para interrupção (melhoria simples no algoritmo tradicional, para evitar passagens desnecessárias pelo vetor depois que ele já está ordenado).

Vantagens:

Simples e intuitivo.
Estável.
Pode ser ligeiramente otimizado para listas quase ordenadas.

Desvantagens:

Muito lento para listas grandes.
Muitas comparações e trocas desnecessárias.
Pouco usado na prática.
Uso ideal: Pequenas listas quase ordenadas ou para fins educacionais.

3.Insertion Sort (Ordenação por Inserção)

Como funciona:

Constrói a lista ordenada elemento por elemento. Cada elemento é inserido na posição correta entre os já ordenados, como cartas na mão.

Vantagens:

Simples e intuitivo.
Muito eficiente para listas pequenas ou quase ordenadas.
Estável e in-place (um algoritmo é chamado de in-place quando ele ordena os elementos usando apenas um espaço extra pequeno, sem criar listas ou arrays adicionais grandes).

Desvantagens:

Lento para listas grandes.
Pouco eficiente para dados muito embaralhados.
Uso ideal: Pequenas listas ou listas parcialmente ordenadas.

4.Merge Sort (Ordenação por Intercalação)

Como funciona:

Divide a lista recursivamente até que cada sublista tenha um elemento. Depois intercala as sublistas ordenadamente. Utiliza memória extra. Ou seja, ele divide a lista em partes menores, ordena essas partes e depois junta (intercala) tudo de volta em ordem.

Vantagens:

Muito eficiente.
Estável.
Sempre leva aproximadamente o mesmo tempo para ordenar, não importa se a lista está bagunçada, quase ordenada ou completamente invertida, ele não piora quando os dados estão desordenados.

Desvantagens:

Requer memória extra.
Mais complexo de implementar.
Implementação recursiva pode atingir limite de pilha.
  *Recursão é quando uma função chama a si mesma para resolver um problema menor.*
Uso ideal: Grandes listas ou quando estabilidade é importante.

5.Quick Sort (Ordenação Rápida)

Como funciona:

Escolhe um pivô, divide a lista em elementos menores e maiores que o pivô, e aplica recursivamente a mesma lógica. Junta as partes ordenadas.

Vantagens:

Muito rápido em listas grandes.
Pouco uso de memória (in-place).
Divide e conquista eficiente.

Desvantagens:

Sensível à escolha do pivô (um pivô mal escolhido pode degradar o desempenho)
Não é estável (elementos com o mesmo valor podem ter sua ordem relativa alterada).
Uso de memória na recursão (embora seja in-place, a recursão profunda em listas muito grandes pode causar problemas de pilha)
Uso ideal: Grandes listas desordenadas, quando estabilidade não é necessária.

6.Heap Sort

Como funciona:

Transforma a lista em um max-heap, coloca o maior elemento no final e reconstrói o heap, repetindo até ordenar todos os elementos.

Vantagens:

Complexidade garantida.
In-place, sem necessidade de memória extra significativa.
Bom para listas grandes.

Desvantagens:

Não é estável.
Mais complexo que Bubble ou Insertion.
Estrutura de heap menos intuitiva.
Uso ideal: Grandes listas quando estabilidade não é importante.

7.Counting Sort

Como funciona:

Conta a frequência de cada elemento, constrói uma tabela de contagem e reconstrói a lista ordenada. Funciona melhor com inteiros pequenos.

Vantagens:

Muito rápido para inteiros pequenos.
Estável.
Evita comparações diretas.

Desvantagens:

Só funciona com inteiros não negativos.
Ineficiente para valores grandes.
Requer memória proporcional ao valor máximo.
Uso ideal: Inteiros pequenos em listas grandes.

8.Radix Sort

Como funciona:

Ordena números por dígitos do menos significativo ao mais significativo usando Counting Sort como sub-rotina. Mantém estabilidade.

Vantagens:

Muito rápido para listas de inteiros grandes.
Estável.
Adequado para dados de grande volume.

Desvantagens:

Só para inteiros não negativos ou adaptados.
Requer memória extra.
Mais complexo que algoritmos simples.
Uso ideal: Grandes listas de inteiros com dígitos limitados.

9.Bucket Sort

Como funciona:

É um método de ordenação que divide os dados em grupos menores (chamados baldes) e depois ordena cada grupo separadamente. Depois que cada balde estiver ordenado, o algoritmo junta todos os baldes em sequência, resultando em uma lista completamente ordenada.
Vantagens:

Rápido para dados uniformemente distribuídos
Fácil de combinar com outros algoritmos de ordenação
Permite processamento paralelo (é quando várias tarefas são feitas ao mesmo tempo, usando mais de um processador ou núcleo do computador)
Funciona bem quando o intervalo dos dados é conhecido

Desvantagens:

Desempenho ruim se os dados não forem bem distribuídos
Usa memória extra para os baldes
Difícil escolher o número ideal de baldes
Não é adequado para dados não numéricos
Uso ideal: Dados uniformemente distribuídos entre 0 e 1 ou intervalo conhecido.
