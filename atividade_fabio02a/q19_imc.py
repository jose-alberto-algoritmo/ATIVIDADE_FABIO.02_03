def main(): 
    peso = float(input('Digite seu peso: '))

    altura = float(input('Digite a sua altura: '))


    imc = calculo(peso, altura)


    print(f'O imc é de {imc}')


    print(classificacao(imc))

 











def calculo(peso, altura):
    calculo = peso / (altura ** 2)
    return calculo


def classificacao(imc):
    if imc < 25:
        return 'Está com o peso normal'
    
    elif imc < 30:
        return 'Está obeso'

    else:
        return 'Obesidade mórbida'
    


main()

