def main():
    num_1 = int(input('Digite o primerio número: '))
    num_2 = int(input('Digite o segundo número: '))

    
    resto1 = resto(num_1, num_2)
    
    resultado = calculo(num_1, num_2, resto1)

    print(resultado)







def resto(n1, n2):
    resto = n1 % n2
    return resto



def calculo(n1, n2, resto):
    if resto == 1:
        soma = n1 + n2 + resto
        return f'A soma dos números {n1} e {n2} mais o resto {resto} é igual a {soma}'
    
    
    elif resto == 2:
        if (n1 % 2) == 0 and (n2 % 2) == 0:
            return f'Os números {n1} e {n2} são pares'
        
        elif (n1 % 2) != 0 and (n2 % 2) != 0:
            return f'Os números {n1} e {n2} são ímpares'
        
        elif (n1 % 2) == 0 and (n2 % 2) != 0:
            return f'Os números {n1} e {n2} são par e ímpar, respectivamente'
        
        else :
            return f'Os números {n1} e {n2} são ímpar e par, respectivamente'
        


    elif resto == 3:
        soma = (n1 + n2) * n1
        return f'A soma dos números {n1} e {n2} multiplicado pelo números {n1} é igual a {soma}'
     
    elif resto == 4:
        soma = (n1 + n2) / n2
        return f'A soma dos números {n1} e {n2} dividido pelo número {n2} é igual a {soma}'
    

        

main()

    
        

        
        






