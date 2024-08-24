# TDE1-RPND-lissa
(lissa deguti) TDE 1 - Resolução de Problemas de Natureza Discreta (Turma 2º U) - Ciência da Computação (Noite) - 2024 / 2º Sem

Realizei o projeto com informações do Livro de Jorge Zavaleta (Professor da Universidade Federal Rural do
Rio de Janeiro), "Modelagem e Simulação de Sistemas Usando Lógica Fuzzy com Python, Teoria e Prática".

Link para o PDF do livro:
https://www.researchgate.net/profile/Jorge-Zavaleta-2/publication/370527332_Modelagem_e_Simulacao_de_Sistemas_Usando_Logica_Fuzzy_com_Python_Teoria_e_Pratica/links/64ba8522c41fb852dd8e901e/Modelagem-e-Simulacao-de-Sistemas-Usando-Logica-Fuzzy-com-Python-Teoria-e-Pratica.pdf

TDE 1

De acordo com o professor Zavaleta, conjuntos são coleções não ordenadas de objetos sem repetição. Em Python,
existe uma coleção predefinida, chamada de set(), que é considerada a forma mais apropriada de lidar com conjuntos.
Existem vários métodos em Python ao se tratar de set() (conjuntos). Dentre eles, utilizei os métodos abaixo para
a realização do projeto:

s.union(r) - União entre s e r
s.intersection(r) - Interseção entre s e r
s.difference(r) - Diferença entre s e r
list(s) - Os elementos de s numa lista

Para o Produto Cartesiano, apenas utilizei o loop 'for' para acumular todos os pares ordenados em um conjunto.
Alterei um pouco a aparência pedida pelo professor, da saída com os resultados das operações por motvos de organização e estética.

--------------------------------------------------------------------------------------
Erros durante o projeto:
-Utilizar listas (list) ao invés de conjuntos (set);

-Aqui tentei fazer a função do Produto Cartesiano utilizando index. O que descobri depois, não ser necessário:

    def produtoCartesiano(conjunto1, conjunto2):
        conjunto1 = list(conjunto1)
        conjunto2 = list(conjunto2)
        produtoCartesiano = set()
        for i in range(len(conjunto1)):
            x = conjunto1[i]
            for j in range(len(conjunto2)):
                y = conjunto2[j]
                par = (x, y)
                produtoCartesiano.add(par)
        return produtoCartesiano

-Tentei usar lista apenas para a função de Produto Cartesiano:

    #para retornar todos os pontos possíveis (onde a lista1 vai ter a coordenada x e a lista2 a coordenada y)
    for a in len(conjunto1):
        x = conjunto1[a]
        for b in len(conjunto2):
            y = conjunto2[b]
            listaTemporaria = {}
            listaTemporaria.append(x)
            listaTemporaria.append(y)
            resultadoCartesiano.append(listaTemporaria)'''
