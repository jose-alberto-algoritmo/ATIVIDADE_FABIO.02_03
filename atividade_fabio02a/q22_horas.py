def main():
    horas1 = int(input('Digite a hora do ínicio: '))

    minutos1 = int(input('Digite os minutos do ínicio: '))

    horas2 = int(input('Digite a horas do termíno: '))

    minutos2 = int(input('Digite os minutos do termíno: '))


    resultado = horas_min(horas1, minutos1, horas2, minutos2)


    print(coversao(resultado))
    
   







def horas_min(hora1, min1, hora2, min2):
    if ((hora1 >= 1 and hora1 <= 23) and (min1 >= 1 and min1 <= 60)) and ((hora2 >= 1 and hora2 <= 23) and (min2 >= 1 and min2 <= 60)):
        converter_min1 = hora1 * 60
        converter_min2 = hora2 * 60
        resultado_minutos = (converter_min2 + min2) - (converter_min1 + min1)
        
        return resultado_minutos
    
    else :
        
        soma =  1440 - ((hora1 * 60) + min1)
        return soma
    

        

def coversao(minuto):
    horas = minuto // 60
    minutos = minuto % 60


    return f'A duração do jogo foi de {horas} horas e {minutos} minutos'

    
    






main()
    



        
    


    




















