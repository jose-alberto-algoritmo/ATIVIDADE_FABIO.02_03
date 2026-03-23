def main():

    print('**sistema triângulo**')

    lado1 = int(input("Digite o lado1: "))
    lado2 = int(input("Digite o lado2: "))
    lado3 = int(input("Digite o lado3: "))

    if eh_triangulo(lado1, lado2, lado3):
        print('É um triângulo')

        print(tipo(lado1, lado2, lado3))



    else: 
        print('não é triângulo')










def eh_triangulo(l1, l2, l3):
    if (l2 + l3) > l1 and (l1 + l3) > l2 and (l1 +l2) > l3:
        return True
    else:
        return False 



def tipo(l1, l2, l3):
    if l1 == l2 and l2 == l3:
        return 'Esse triângulo é do tipo equilátero'
    
    elif l1 != l2 and l2 != l3:
        return 'Esse triângulo é do tipo escaleno'
    else:
        return 'Esse triângulo é do tipo isósceles'





main()