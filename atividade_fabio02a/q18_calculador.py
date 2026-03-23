def main():
    print('**calculadora**')

    numero1 = int(input('Digite o primero número: '))
    numero2 = int(input('Digite o segundo número: '))

    print('1-Adição')
    print('2-subtração')
    print('3-multiplicação')
    print('4-divisão')
    
    opcao = int(input('Digite a operação desejada: '))


    print(calcular(opcao, numero1, numero2))






def calcular(op, n1, n2):
    if op == 1:
        soma = n1 + n2
        return f'A soma dos números {n1} e {n2} é igual a {soma}'
    
    elif op == 2:
        subtracao = n1 - n2
        return f'A subtracão dos números {n1} e {n2} é igual a {subtracao}'
    
    elif op == 3:
        multiplicacao = n1 * n2
        return f'A multiplicação dos números {n1} e {n2} é igual a {multiplicacao}'
    elif op == 4:
        divisao = n1/n2
        return f'A divisão dos números {n1} e {n2} é igual a {divisao}'
    
    else:
        print('Erro, insira o valor corretamente.')




main()













