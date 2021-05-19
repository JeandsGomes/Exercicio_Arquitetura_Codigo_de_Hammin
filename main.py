from Exercicio_Arquitetura import exercicio_arquitetura

Cod_Hammi=exercicio_arquitetura()

def interface_inicial():
    print('Qual operacao voce deseja realizar:')
    return int(input('0 - GERAR A CODIFICAÇÃO DE HAMMING\n1 - AVALIADOR DE CÓDIGO DE HAMMING\n2 - Sair\n>> '))

def interface_gerar_hamming():
    print('GERAR A CODIFICAÇÃO DE HAMMING')
    codigo = input('Informe o codigo: ')
    codigo_hammi = Cod_Hammi.Codigo_de_Hammin(Cod_Hammi.ampliando(codigo))
    print('Codigo de Hammi gerado : {}'.format(Cod_Hammi.lista_binario_str(codigo_hammi)))
    input('PRECIONE ENTER PARA CONTINUAR...')
    print('\n\n')

def interface_avaliar_erro_em_hamming():
    print('AVALIADOR DE CÓDIGO DE HAMMING')
    codigo_hammi = input('Informe o codigo de Hammin: ')
    posicao_errada = Cod_Hammi.Posicao_do_erro(codigo_hammi)
    
    if(posicao_errada != -1):
        print('O codigo possui erro na posicao : {}'.format(posicao_errada))
        codigo_hammi_corrigido = Cod_Hammi.inverter_bit_errado(posicao_errada,list(codigo_hammi))
        print('Correcao do codigo: {}'.format(Cod_Hammi.lista_binario_str(codigo_hammi_corrigido)))
    else:
        print('Codigo não possui erro!!!')
    
    input('PRECIONE ENTER PARA CONTINUAR...')
    print('\n\n')

def main():

    while(True):
        operacao = interface_inicial()
        if(operacao == 0):
            interface_gerar_hamming()
        elif(operacao == 1):
            interface_avaliar_erro_em_hamming()
        elif(operacao == 2):
            print('Programa finalizado!!!')
            break

if __name__=="__main__":
    main()

