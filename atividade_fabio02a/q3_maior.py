def main():
    n1 = obter_numero("Digite o primeiro número: ")
    n2 = obter_numero("Digite o segundo número: ")
    n3 = obter_numero("Digite o terceiro número: ")

    verificar = eh_maior(n1, n2, n3)

    escrever(verificar)




def obter_numero(valor):
    numero = int(input(valor))
    return numero

def eh_maior(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return f'{n1} é o maior número'
    elif n2 > n1 and n2 > n3:
        return f'{n2} é o maior número'
    elif n1 == n2 and n1 == n3:
        return 'Todos os números são iguais'
    else:
        return f'{n3} é o maior número'
    

def escrever(conteudo):
    escrever = print(conteudo)
    return escrever

main()