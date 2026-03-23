def main():

    angulo1 = obter_numero("Digite o ângulo1: ")
    angulo2 = obter_numero("Digite o ângulo2: ")
    angulo3 = obter_numero("Digite o ângulo3: ")



    if eh_triangulo(angulo1, angulo2, angulo3):
        print('É triângulo')

        
        if tipo_acutangulo(angulo1, angulo2, angulo3):
            print('Esse triângulo é um acutângulo')
        
        
        if tipo_retangulo(angulo1, angulo2, angulo3):
            print("Esse triângulo é do tipo retângulo")


    
    else:
        print('Não é triângulo')






    







   

def obter_numero(descricao):
    numero = int( input(descricao))
    return numero


def eh_triangulo(an1, an2, an3):
    if (an1 + an2 + an3) == 180:
        return True 
    else:
        return False 
    
def tipo_acutangulo(ang1, ang2, ang3):
    if 90 > ang1 and 90 > ang2 and 90 > ang3:
        return True 
    else:
        return False 
    
def tipo_retangulo(ang1, ang2, ang3):
    if ang1 == 90 or ang2 == 90 or ang3 == 90:
        return True 
    else:
        False


main()







