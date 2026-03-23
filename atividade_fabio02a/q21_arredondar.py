def main(): 

    inteiro = int(input('Digite a parte inteira: '))

    fracionada = float(input('Digite a parte decimal: '))


    resultado = arredondamento(inteiro, fracionada)

    numero_soma = inteiro + fracionada

    print(f'O arredondamento do número {numero_soma} é {resultado}')







def arredondamento(inteiro, decimal):
    if decimal >= 0.5:
        soma = inteiro + 1
        return soma
    else :
        return inteiro

main()
    