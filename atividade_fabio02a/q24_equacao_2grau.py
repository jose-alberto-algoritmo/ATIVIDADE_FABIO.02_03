def main():
    print ('***Equação do segundo grau***')

    print()

    a = int(input('Digite o coeficiente A:'))
    b = int(input('Digite o coeficiente b: '))
    c = int(input('Digite o coeficiente c: '))

    resultado = equacao(a, b, c)

    print(resultado)







def equacao(a, b, c):
    if a != 0:
        delta = (b**2)-4*a*c

        x1 = (-(b) + (delta**0.5)) / (2*a)
        x2 = (-(b) - (delta**0.5)) / (2*a)

        return f'x1 = {x1} e x2 = {x2}'

        
    
    else:
        return 'valor iválido'
        












































main()
