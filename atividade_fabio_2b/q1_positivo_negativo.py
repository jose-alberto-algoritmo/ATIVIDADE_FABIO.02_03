def main():
    numero = int(input('Digite o número: '))


    print(verficar_sinal(numero))














def verficar_sinal(numero):
    if numero < 0:
        return f'O número {numero} é negativo'
    
    else:
        return f'O número {numero} é positivo'
    




main()



