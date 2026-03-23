def main():
    numero = int(input('Digite o número: '))


    verifcar_primo = primo(numero)

    escrever(verifcar_primo)







def primo(numero):
    if (numero != 5) and (numero != 2) and (numero != 3) and (numero != 7) and ((numero % 2) == 0) or ((numero % 3)) == 0 or ((numero % 5 )) == 0 or ((numero % 7)) == 0:
        return f'O {numero} não é número primo'
    else: 
        return f'O {numero} é número primo'


def escrever(conteudo):
    escrever = print(conteudo)
    return escrever






main()


