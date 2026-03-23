def main():

    print('***Digite a primeira coordenada*** ')

    y1 = int(input('Digite o ponto do eixo y1: '))

    x1 = int(input('Digite o ponto do eixo x1: '))


    print('***Digite a segunda coordenada*** ')

    y2 = int(input('Digite o ponto do eixo y2: '))

    x2 = int(input('Digite o ponto do eixo x2: '))


    base = (x1) - (x2)
    altura = (y2) - (y1)

    conversao_base = calcular_base(base)
    calcula_altura = calcular_altura(altura)

    resultado = calcula_altura * conversao_base

    print(f'A área é igual a {resultado}')











def area(base, altura):
    area = base * altura
    return area


def calcular_base(base):

    if base < 0:
        soma = (base) * (-1)
        return soma
    
    else :
        return base
        

        
    
    
def calcular_altura(altura):
    if altura < 0:
        soma = (altura) * (-1)
        return soma
    
    else:
        return altura
    


    





main()











