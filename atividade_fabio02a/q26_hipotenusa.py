def main():

    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    num3 = int(input('Digite o terceiro número: '))

    resultado = verificar_hipotenusa(num1, num2, num3)

    print(resultado)
















def verificar_hipotenusa(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return f'{n1} é a hipotenusa e {n2}, {n3} são os catetos'
    
    elif n2 > n1 and n2 > n3:
        return f'{n2} é a hipotenusa e {n1}, {n3} são os catetos'
    
    else :
        return f'{n3} é a hipotenusa e {n2}, {n1} são os catetos'
    

main()