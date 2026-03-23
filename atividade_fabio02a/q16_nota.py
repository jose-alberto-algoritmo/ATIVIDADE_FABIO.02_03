def main():
    nota_1 = float(input('Digite a nota1: '))

    nota_2 = float(input('Digiti a nota2: '))

    
    resultado_media = media(nota_1, nota_2)

    
    
    
    if resultado_media < 7:
        
        exame = float(input('Digite a nota do exame: '))

        calculo = (exame + resultado_media) / 2

        
        if calculo >= 5:
            
            print(f'A média final é {calculo}, aprovado')

        
        else:
            print(f'A média final é {calculo}, reprovado')

        

    else: 
        print(f'A média das notas é {resultado_media}, aprovado')
        
        



    


def media(n1, n2):
    media = (n1 + n2) / 2
    return media 



main()
