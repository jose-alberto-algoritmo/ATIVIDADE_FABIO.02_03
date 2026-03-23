def main():


    produto_1 = float(input('Digite o preço do primerio produto: '))

    produto_2 = float(input('Digite o preço do segundo produto: '))
    
    produto_3 = float(input('Digite o preço do terceiro produto: '))

    resultado = mais_barato(produto_1, produto_2, produto_3)

    print(resultado)















def mais_barato(produt1, produt2, produt3):
    
    if produt1 < produt2 and produt1 < produt3:
        return 'O primerio produto é o mais barato'
        
    elif produt2 < produt1 and produt2 < produt3:
        return 'O segundo produto é o mais barato'
        
    elif produt3 < produt1 and produt3 < produt2:
        return 'O terceiro produto é o mais barato'
        
    else:
        return 'Os três produtos tem o mesmo preço'
        





main()














