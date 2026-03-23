def main():

    
    
    number1 = int(input('Digite o number1: '))
    number2 = int(input('Digite o number2: '))
    number3 = int(input('Digite o number3: '))


    opcao = int(input('Digite um número de 1 a 3: '))



    number_resultado = number_calcular(opcao, number1, number2, number3)

    print(number_resultado)




def number_calcular(op, n1, n2, n3):
    if op == 1:
        return n1
    elif op == 2:
        return n2
    elif op ==3:
        return n3
    else:
        return 'Número não correspondido'







main()





