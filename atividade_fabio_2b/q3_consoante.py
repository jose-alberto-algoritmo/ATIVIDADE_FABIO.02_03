def main():

    letra = str(input('Digite a letra: '))

    resultado = verificar(letra)

    print(resultado)












def verificar(letra):
    if letra == 'A' or letra == 'a':
        return 'É vogal'
    
    elif letra == 'E' or letra == 'e':
        return 'É vogal'
    
    elif letra == 'I' or letra == 'i':
        return 'É vogal'
    
    elif letra == 'O' or letra == 'o':
        return 'É vogal'
    
    elif letra == 'U' or letra == 'u':
        return 'É vogal'
    
    else:
        return 'É consoante'
    



main()







