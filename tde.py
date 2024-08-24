#AUTOR: Lissa Deguti
#funções
def uniao(conjunto1, conjunto2):
    return conjunto1.union(conjunto2)

def intersecao(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)

def diferenca(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)

def produtoCartesiano(conjunto1, conjunto2):
    produtoCartesiano = set()
    for a in conjunto1:
        for b in conjunto2:
            par = (a, b)
            produtoCartesiano.add(par)
    
    return produtoCartesiano

#---------------------------------------------------------
# !!!!MUDE AQUI O NOME DO ARQUIVO PARA TESTE DE CÓDIGO!!!!
#---------------------------------------------------------

#dentro do "with open", o arquivo txt está sendo acessado
with open("operacoes1.txt", "r") as arquivo: #alterar o nome do arquivo (operacoes1.txt, operacoes2.txt, operacoes3.txt)
    linhas = arquivo.readlines() 
    qntdOperacoes = int(linhas[0].strip()) #lê a primeira linha para saber a quantidade de operações

    linhaAtual = 1
    for a in range(qntdOperacoes):
        tipoOperacao = (linhas[linhaAtual].strip())
    
        conjunto1 = set(linhas[linhaAtual + 1].strip().split(", "))
        conjunto2 = set(linhas[linhaAtual + 2].strip().split(", "))
    
        if tipoOperacao == "U":
            nomeOperacao = "União"
            resultado = uniao(conjunto1, conjunto2)
        elif tipoOperacao == "I":
            nomeOperacao = "Interseção"
            resultado = intersecao(conjunto1, conjunto2)
        elif tipoOperacao == "D":
            nomeOperacao = "Diferença"
            resultado = diferenca(conjunto1, conjunto2)
        elif tipoOperacao  == "C":
            nomeOperacao = "Produto Cartesiano"
            resultado = produtoCartesiano(conjunto1, conjunto2)
        
    
        print(f"{nomeOperacao}: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}")
        
        linhaAtual += 3

