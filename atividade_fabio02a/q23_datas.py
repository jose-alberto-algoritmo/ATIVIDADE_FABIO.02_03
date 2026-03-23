def main():
    print()
    
    print('**Digite a primera data**')
    
    print()
    print()
    
    dia1 = int(input('Digite o dia: '))
    mes1 = int(input('Digite o mês: '))
    ano1 = int(input('Digite o ano: '))
    print()
    print()
    
    print('**Digite a segunda  data**')
    print()
    print()
    dia2 = int(input('Digite o dia: '))
    mes2 = int(input('Digite o mês: '))
    ano2 = int(input('Digite o ano: '))




    resultado = vericar_recente(ano1, mes1, dia1, ano2, mes2, dia2)

    print(resultado)










def vericar_recente(ano1, mes1, dia1, ano2, mes2, dia2):
    if (ano1 >= 1 and ano1 <= 2026) and (ano2 >= 1 and ano2 <= 2026) and (mes1 >= 1 and mes1 <= 12) and (mes2 >= 1 and mes2 <= 30) and (dia1 >= 1 and dia1 <= 30) and (dia2 >= 1 and dia2 <= 30):
        
        if (ano1 == ano2) and (mes1 == mes2) and (dia1 == dia2):
            return f'As datas {dia1}/{mes1}/{ano1} e {dia2}/{mes2}/{ano2} são iguais'
        
        elif ano1 > ano2 :
            return f'A data {dia1}/{mes1}/{ano1} é mais recente que a data {dia2}/{mes2}/{ano2}'
        
        elif ano2 > ano1 :
            return f'A data {dia2}/{mes2}/{ano2} é mais recente que a data {dia1}/{mes1}/{ano1}'
        
        elif (ano1 == ano2) and (mes1 > mes2) :
            return f'A data {dia1}/{mes1}/{ano1} é mais recente que a data {dia2}/{mes2}/{ano2}'
        
        elif (ano1 == ano2) and (mes2 > mes1):
            return f'A data {dia2}/{mes2}/{ano2} é mais recente que a data {dia1}/{mes1}/{ano1}'
        
        elif (ano1 == ano2) and (mes1 == mes2) and (dia1 > dia2):
            return f'A data {dia1}/{mes1}/{ano1} é mais recente que a data {dia2}/{mes2}/{ano2}'
        
        elif (ano1 == ano2) and (mes1 == mes2) and (dia2 > dia1):
            return f'A data {dia2}/{mes2}/{ano2} é mais recente que a data {dia1}/{mes1}/{ano1}'

            
        
        



    else:
        return 'Essa data não é válida'



main()
