def main():
    numero = (int(input('Digite o número: ')))

    dezena_1 = numero // 100

    dezena_2 = numero % 100

    resultado = calcular(dezena_1, dezena_2)


    print(resultado)










def calcular(dez1, dez2):
    soma = dez1 + dez2

    quadrado = soma ** 2
    return quadrado







main()






