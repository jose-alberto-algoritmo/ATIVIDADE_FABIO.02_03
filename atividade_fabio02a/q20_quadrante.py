def main():

    angulo = int(input('Digite o ângulo: '))


    print(quadrante(angulo))






def quadrante(angulo):
    if angulo > 0 and angulo < 90:
        return 'Primerio quadrante'
    
    elif angulo > 90 and angulo < 180:
        return 'segundo quadrante'
    
    elif angulo > 180 and angulo < 270:
        return 'Terceiro quadrante'
    
    else:
        return 'Quarto quadrante'
    



main()











