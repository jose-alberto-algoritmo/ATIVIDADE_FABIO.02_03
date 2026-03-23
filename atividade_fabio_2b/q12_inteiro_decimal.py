def main():

    numero = float(input('Digie o número: '))
    
    
    print(verificar(numero))

















def verificar(numero):
    if numero % 1 == 0:
        return ' Esse número é inteiro'
    
    else :
        return 'Esse número é decimal'


















main()