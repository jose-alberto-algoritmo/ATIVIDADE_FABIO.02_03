def main():
    numero1 = int(input("Digite o número1: "))
    numero2 = int(input("Digite o número2: "))
    numero3 = int(input("Digite o número3: "))
    numero4 = int(input("Digite o número4: "))
    numero5 = int(input("Digite o número5: "))


    maximo = maior(numero1, numero2, numero3, numero4, numero5)

    minimo = menor(numero1, numero2, numero3, numero4, numero5)


    print(f'O maior número é {maximo} e o menor número é {minimo} ')

    



def maior(n1, n2, n3, n4, n5):
    if varificar_maior(n1, n2, n3, n4, n5):
        return n1
    elif varificar_maior(n2, n1, n3, n4, n5): 
        return n2

    elif varificar_maior(n3, n2, n1, n4, n5): 
        return n3
    
    elif varificar_maior(n4, n2, n3, n1, n5):
        return n4 
    else : 
        return n5


def menor(n1, n2, n3, n4, n5):
    if varificar_menor(n1, n2, n3, n4, n5):
        return n1
    elif varificar_menor(n2, n1, n3, n4, n5): 
        return n2

    elif varificar_menor(n3, n2, n1, n4, n5): 
        return n3
    
    elif varificar_menor(n4, n2, n3, n1, n5):
        return n4 
    else : 
        return n5










def varificar_maior(n1, n2, n3, n4, n5):
    if n1 > n2 > n3 > n5:
        return n1
    


def varificar_menor(n1, n2, n3, n4, n5):
    if n1 < n2 < n3 < n5:
        return n1
    



main()



