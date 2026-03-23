def main():

    senha = int(input('Digite a senha de 3 dígitos: '))


    num_1 = senha // 100
    resto = senha % 100
    num_2 = resto // 10
    num_3 = resto % 10

    resultado =  verificar_senha(num_1, num_2, num_3)

    print(resultado)






def verificar_senha(n1, n2, n3):
    if n1 == 1 and n2 == 2 and n3 == 3:
        return 'Acesso permitido'
    
    else:
        return 'Acesso negado'





main()





