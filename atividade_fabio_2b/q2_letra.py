def main():

    letra = str(input('Digite a letra: '))

    resultado = verificar(letra)
    
    print(resultado)







def verificar(letra):
    if letra == 'M' or letra == 'm':
        return 'sexo masculino'
    
    elif letra == 'F' or letra == 'f':
        return 'sexo feminino'
    
    else:
        return 'sexo iválido'



main()







