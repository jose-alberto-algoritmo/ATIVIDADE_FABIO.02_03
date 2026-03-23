def main():

    numero = (int(input('Digite o número da semana: ')))


    print(dia_semana(numero))













def dia_semana(numero):
    if numero == 1:
        return 'É domingo'
    
    elif numero == 2:
        return 'É sengunda-feira'
    
    elif numero == 3:
        return 'É terça-feira'
    
    elif numero == 4:
        return 'É quarta-feira'
    
    elif numero == 5:
        return 'É quinta-feria'
    
    elif numero == 6:
        return 'É sexta-feira'
    
    elif numero == 7:
        return 'É sábado'
    
    else :
        return 'Valor inválido'





main()
