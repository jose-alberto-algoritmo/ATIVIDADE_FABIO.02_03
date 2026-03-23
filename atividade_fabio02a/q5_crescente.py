def main():

    n = obter_numero("Digite três números: ")
    
    centena = n // 100
    resto = n % 100
    dezena = resto // 10
    unidade = resto % 10


    verificar = crescente(centena, dezena, unidade)

    escrever(verificar)


def escrever(descricao):
    conteudo = print(descricao)
    return conteudo


def obter_numero(descricao):
    numero = int(input(descricao))
    return numero


def crescente(a, b,c ):
    if a > b and b > c:
        return f'Esse número escrito de forma crescente é {c}{b}{a}'
    elif b > a and a > c:
        return f'Esse número escrito de forma crescente é {c}{a}{b}'
    elif c > a and a > b:
        return f'Esse número escrito de forma crescente é {b}{a}{c}'
    elif a > c and c > b :
        return f'Esse número escrito de forma crescente é {b}{c}{a}'
    elif c > b and b > a:
        return f'Esse número escrito de forma crescente é {a}{b}{c}'
    else:
        return f'Esse número escrito de forma crescente é {a}{c}{b}'
    



main()

