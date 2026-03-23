def main():

    numero = int(input('Digite o número de três dígitos: '))

    

    escrever(verificar(numero))




    







def verificar(numero):
    if numero < 1000:
        
        centena = numero // 100
        resto = numero % 100
        dezena = resto // 10
        unidade = resto % 10

        return f'{centena} centenas, {dezena} dezenas {unidade} unidades'
    
    else:
        return 'O número é inválido'
     

def escrever(conteudo):
    escrever = print(conteudo)
    return escrever
































main()