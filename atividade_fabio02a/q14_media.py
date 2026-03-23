def main():
    num_1 = float(input('Digite o número1: '))
    num_2 = float(input('Digite o número2: '))
    num_3 = float(input('Digite o número3: '))
    num_4 = float(input('Digite o número4: '))
    num_5 = float(input('Digite o número5: '))



    media_resultado = media(num_1, num_2, num_3, num_4, num_5)

    eh_maior = eh_maior_q_media(media_resultado,num_1, num_2, num_3,num_4, num_5)

    print(f'A média dos números são {media_resultado}')

    print(eh_maior)








def media(n1, n2, n3, n4, n5):
    media = (n1 + n2 + n3 + n4 + n5) / 5
    return media 



def eh_maior_q_media(media, n1, n2, n3, n4, n5):
    if n1 > media:
        return f'O número {n1} é maior que a média'
    
    elif n2 > media:
        return f'O número {n2} é maior que a média'
    elif n3 > media:
        return f'O número {n3} é maior que a média'
    elif n4 > media:
        return f'O número {n4} é maior que a média'
    elif n5 > media:
        return f'O número {n5} é maior que a média'
    else :
        return f'Todos os números são iguais'

    


main()
