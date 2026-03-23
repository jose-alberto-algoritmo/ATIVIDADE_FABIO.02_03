def main():

    n1 = obter_numero("Digite o número: ")

    dezena = n1 // 10
    unidade = n1 % 10

    verificar = eh_igual(dezena, unidade)
    
    escrever(verificar)


def obter_numero(descricao):
    numero = int(input(descricao))
    return numero


def eh_igual(dezena, unidade):
    if dezena == unidade:
        return 'A dezena é igual a unidade'
    else:
        return 'A dezena é diferente da unidade'
    

def escrever(conteudo):
    escrever = print(conteudo)
    return escrever


main()