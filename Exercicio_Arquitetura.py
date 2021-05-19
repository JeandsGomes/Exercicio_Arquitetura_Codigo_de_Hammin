



class exercicio_arquitetura():

    def __init__(self):
        pass

    def ampliando(self,codigo):
        contador_index = 0
        contador_index_codigo = 0
        contador_potencias_2 = 0
        codigo_lis = list(codigo)
        codigo_ampliado = []

        while(contador_index_codigo < len(codigo_lis)):
            contador_index += 1
            if(contador_index == (2**contador_potencias_2)):
                codigo_ampliado.append('x')
                contador_potencias_2 += 1
            else:
                codigo_ampliado.append(codigo_lis[contador_index_codigo])
                contador_index_codigo += 1

        return codigo_ampliado

    def reduzindo(self,codigo_ampliado):
        contador_potencias_2 = 0
        codigo_reduzido = []

        for contador_index in range(0,len(codigo_ampliado)):
            if(contador_index+1 == (2**contador_potencias_2)):
                contador_potencias_2 += 1
            else:
                codigo_reduzido.append(codigo_ampliado[contador_index])

        return codigo_reduzido



    def paridade_lista(self,posicao_bit_verificacao,codigo_ampliado):
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

    def paridade_valor_lista(self,paridade_lista):
        contador_de_1 = 0
        for elemento in paridade_lista:
            if(elemento == '1'):
                contador_de_1 += 1

        if(contador_de_1%2 == 0):
            return '0'
        else:
            return '1'

    def Codigo_de_Hammin(self,codigo_ampliado):
        for i in range(0,len(codigo_ampliado)):
            if(codigo_ampliado[i]=='x'):
                codigo_ampliado[i] = self.paridade_valor_lista(self.paridade_lista(i,codigo_ampliado))
        return codigo_ampliado
        
    def inverter_lista(self,lista):
        lista_invertida = []
        for index in range(len(lista)-1,-1,-1):
            lista_invertida.append(lista[index])
        return lista_invertida

    def lista_binario_decimal(self,lista_binario):
        string_binario = ''
        for bit in lista_binario:
            string_binario=string_binario + bit

        return int(string_binario,2)

    def lista_binario_str(self,lista_binario):
        string_binario = ''
        for bit in lista_binario:
            string_binario=string_binario + bit
        
        return string_binario        

    def paridade_valor_lista_mais_bit(self,bit,paridade_lista):
        contador_de_1 = 0
        if(bit == '1'):
            contador_de_1 += 1

        for elemento in paridade_lista:
            if(elemento == '1'):
                contador_de_1 += 1

        if(contador_de_1%2 == 0):
            return '0'
        else:
            return '1'

    def posicao_bits_verificacao(self,codigo_de_hammin):
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

    def Posicao_do_erro(self,codigo_de_hammin):

        posicao_bits_verificacao_paridade = self.posicao_bits_verificacao(self.reduzindo(codigo_de_hammin))
        posicao_do_erro = []
        
        for i in posicao_bits_verificacao_paridade:
            valores_para_paridade = self.paridade_lista(int(i)-1,codigo_de_hammin)
            
            paridade = self.paridade_valor_lista_mais_bit(codigo_de_hammin[int(i)-1],valores_para_paridade)
            posicao_do_erro.append(paridade)

        if('1' in posicao_do_erro):
            return self.lista_binario_decimal(self.inverter_lista(posicao_do_erro))
        else:
            return -1
            
    def inverter_bit_errado(self,posicao_errada,codigo_de_hammin):
        
        if(codigo_de_hammin[posicao_errada-1]=='0'):
            codigo_de_hammin[posicao_errada-1]='1'
            return codigo_de_hammin
        else:
            codigo_de_hammin[posicao_errada-1]='0'
            return codigo_de_hammin

