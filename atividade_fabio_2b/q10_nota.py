def main():
    
    nota1 = float(input('Digita primeira nota: '))

    nota2 = float(input('Digite a segunda nota: '))


    media = (nota1 + nota2) / 2


    
    print(f'Média: {media}            {nota_letra(media)}')

    print()
    print()
    
    print(f'Situação: {situacao(nota_letra(media))}')










    

def nota_letra(media):
    if media > 9 and media <= 10:
        return 'A'
    
    elif media > 7.5 and media < 9:
        return 'B'
    
    elif media > 6 and media < 7.5:
        return 'C'
    
    elif media > 4 and media < 6:
        return 'D'
    
    elif media > 0 and media < 4:
        return 'E'
    
    else :
        return 'I'


def situacao(letra):
    if letra == 'A' or letra == 'B' or letra == 'C':
        return 'Aprovado'
    
    elif letra == 'D' or letra == 'E':
        return 'Reprovado'
    
    else :
        return 'Nota inválida'


main()

