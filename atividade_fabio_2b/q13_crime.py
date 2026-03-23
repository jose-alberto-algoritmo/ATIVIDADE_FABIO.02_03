def main():
    pergunta_1 = input('Telefonou para a vítima? ')

    pergunta_2 = input('Esteve no local do crime? ')

    pergunta_3 = input('Mora perto da vítima? ')

    pergunta_4 = input('Devia para a vítima?')

    pergunta_5 = input('Já trabalhou com a vítima? ')


    resultado_quantidade = quantidade(pergunta_1, pergunta_2, pergunta_3, pergunta_4, pergunta_5)

    resultado = resposta(resultado_quantidade)

    print(resultado)

  





def quantidade(per_1, per_2, per_3, per_4, per_5):

    if per_1 == 'sim' or per_1 == 'SIM' or per_1 == 'Sim':
        numero1 = 1
    else :
        numero1 = 0


    if per_2 == 'sim' or per_2 == 'SIM' or per_2 == 'Sim':
        numero2 = 1

    else :
        numero2 = 0

    
    
    if per_3 == 'sim' or per_3 == 'SIM' or per_3 == 'Sim':
        numero3 = 1
    else :
        numero3 = 0

    
    
    if per_4 == 'sim' or per_4 == 'SIM' or per_4 == 'Sim':
        numero4 = 1
    else :
        numero4 = 0

    
    
    if per_5 == 'sim' or per_5 == 'SIM' or per_5 == 'Sim':
        numero5 = 1
    
    else :
        numero5 = 0

    
    soma = numero1 + numero2 + numero3 + numero4 + numero5

    return soma 

        

def resposta(numero):

    if numero == 0 or numero == 1:
        return 'Inocente'
    
    elif numero == 2:
        return 'Suspeito'
    
    elif numero >= 3 and numero < 5: 
        return 'cúmplice'
    
    else :
        return 'É o assassino '




main()

