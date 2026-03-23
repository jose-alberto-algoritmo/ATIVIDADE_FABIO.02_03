def main():
    numero = int(input('Dgite o número: '))

    dezena_1 = numero // 100
    dezena_2 = numero % 100

    resultado = quadrado_perf(numero, dezena_1, dezena_2)

    print(resultado)
    





def quadrado_perf(numero, dez1, dez2):
    raiz = numero**0.5
    soma_dez = dez1 + dez2

    if raiz == soma_dez:
        
        return f'O número {numero} possui quadrado perfeito'
    
    else :
        return f'O número {numero} não possui quadrado perfeito'





main()





