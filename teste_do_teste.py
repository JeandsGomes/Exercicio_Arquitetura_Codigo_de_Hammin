
def paridade_lista(posicao_bit_verificacao,codigo_ampliado):
    contador_posicao = 0
    paridade = []

    posicoes = []
    
    flag = 1
    for index in range(posicao_bit_verificacao,len(codigo_ampliado)):

        if(index != posicao_bit_verificacao):

            if(contador_posicao==(posicao_bit_verificacao+1)):
                flag = 0
            elif(contador_posicao==0):
                flag = 1

            if(flag == 1):
                paridade.append(codigo_ampliado[index])
                posicoes.append(index)
                contador_posicao += 1

            elif(flag == 0):
                contador_posicao -= 1
        
        else:
            contador_posicao += 1

    return paridade

print(paridade_lista(0,list('0101100')))