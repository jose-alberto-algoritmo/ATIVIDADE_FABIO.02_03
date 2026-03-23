def main():

    letra = str(input('Digite a letra do turno: '))

    resultado = turno(letra)

    print(resultado)















def turno(letra):
    if letra == 'M' or letra == 'm':
        return 'Bom dia!'
    
    elif letra == 'V' or letra == 'v':
        return 'Boa tarde!'
    
    elif letra == 'N' or letra == 'n':
        return 'Boa noite!'
    
    else :
        return 'valor inválido'
        


main()



