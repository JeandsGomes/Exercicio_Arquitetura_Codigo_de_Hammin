def posicao_bits_verificacao(codigo_de_hammin):
    contador_index = 0
    contador_index_codigo = 0
    contador_potencias_2 = 0
    codigo_lis = list(codigo_de_hammin)
    posicao_bits_verificacao = []

    while(contador_index_codigo < len(codigo_lis)):
        contador_index += 1
        if(contador_index == (2**contador_potencias_2)):
            posicao_bits_verificacao.append(str(contador_index))
            contador_potencias_2 += 1
        else:
            contador_index_codigo += 1

    return posicao_bits_verificacao

a=posicao_bits_verificacao(list('00111'))

print(a)