
def main():

    n1 = obter_numero('Digite o primeiro número: ')
    n2 = obter_numero('Digite o segundo número: ')

    verficar = menor_maior(n1, n2)

    escrever(verficar)


  


def obter_numero(descricao):
    numero = int(input(descricao))
    return numero


def menor_maior(n1, n2):
    if n1 > n2:
        return f'{n1} é maior que {n2}'
    elif n1 == n2:
        return f'{n1} é igual a {n2}'
    else:
        return f'{n2} é maior que {n1}'
    

def escrever(conteudo):
    escrever = print(conteudo)

main()