def main():
    numero1 = obter_numero('Digite o primeiro número: ')
    numero2 = obter_numero('Digite o segundo número: ')
    numero3 = obter_numero('Digite o terceiro número: ')

    verficar = eh_igual(numero1, numero2, numero3)

    escrever(verficar)







def eh_igual(n1, n2, n3):
    if n1 == n2 and n1 == n3:
        return "Todos os números são iguais"
    
    elif n1 != n2 and n1 != n3 and n2 != n3:
        return 'Todos os números são diferentes'
    
    else:
        return ' Dois números são iguais'
    


def obter_numero(valor ):
    numero = int(input(valor))
    return numero



def escrever(conteudo):
    escrever = print(conteudo)
    return escrever



main()