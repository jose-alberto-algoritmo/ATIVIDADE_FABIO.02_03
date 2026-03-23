def main():

    anoatual = int(input("digite o ano atual: "))
    mesatual = int(input('digite o mês atual: '))
    diasatual = int(input('digite os dia atual: '))

    #nascimento
    anos_na = int(input('digite o ano de nascimento: '))
    meses_na =  int(input('digite o mês de nasmento: '))
    dias_na = int(input('digite o dia do nascimento: '))

    anos = calcular_ano(anoatual, anos_na)
    
    mes_dia = calcula_mes_dia(mesatual, meses_na,diasatual, dias_na )
    
    soma = anos + mes_dia

    print(f'A idade exata é de {soma}')








def calcular_ano(anoatual, ano_nascimento):
    ano = anoatual - ano_nascimento
    return ano


def calcula_mes_dia(mesatual, mes_nascimento, diaatual, dia_nascimento):
    
    if mesatual >= mes_nascimento and diaatual >= dia_nascimento:
        return 0
    else:
        return -1
    


main()




