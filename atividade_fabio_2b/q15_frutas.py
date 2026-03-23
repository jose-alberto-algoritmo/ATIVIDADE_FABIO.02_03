def main():
    print()
    print()
    

    maca_kg = float(input('Digite a quantidade de maçã desejada kg: '))

    morango_kg = float(input('Digite a quantidade de morango desejada kg: '))


    preco_maca = maça_preco(maca_kg)
    
    
    preco_morango = morango_preco(morango_kg)

    
    preco_total = preco_maca + preco_morango

    
    kilo_total = maca_kg + morango_kg

    
    
    
    
    if preco_total > 25 or kilo_total > 8:
        desconto = preco_total - (preco_total * 0.10)

        print(f'O valor total deu {preco_total}, mas teve um desconto de 10%,então agora equivale a {desconto}')

    else :

        print(f'o valor total deu {preco_total}')










def morango_preco(morango_kg):
    if morango_kg > 0 and morango_kg <=5:
        preco = morango_kg * 2.50

        return preco

    elif morango_kg > 5:
        preco2 = morango_kg * 2.20

        return preco2

    else:

        return 'Valor inválido'




def maça_preco(maca):
    if maca > 0 and maca <= 5:
        preco = maca * 1.80

        return preco
    
    elif maca > 5:
        preco2 = maca * 1.50

        return preco2
    
    else :
        return 'Valor inválido'



main()