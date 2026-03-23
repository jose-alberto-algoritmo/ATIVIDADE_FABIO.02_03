def main():
    print()

    print('***Digite a data de nascimento***')

    ano_nas = int(input('Digite o ano: '))
    mes_nas = int(input('Digite o mês: '))
    dia_nas = int(input('Digite o dia:'))

    print()

    print('***Digite a data atual***')

    ano_atual = int(input('Digite o ano: '))
    mes_atual = int(input('Digite o mês: '))
    dia_atual = int(input('Digite o dia: '))

    
    resultado_ano = ano(ano_nas, ano_atual)
    resultado_aniversario =verifcar_aniversario(mes_nas, dia_nas, mes_atual, dia_atual)
    
    
    idade_exata = resultado_ano + resultado_aniversario
    
    print(idade_exata,dia_mes(mes_nas, dia_nas, mes_atual, dia_atual))








def ano(ano_nasc, ano_atual):
    anos = ano_atual - ano_nasc
    return anos


def verifcar_aniversario(mes_nasc, dia_nasc, mes_atual, dia_atual):
    
    if mes_atual >= mes_nasc and dia_atual >= dia_nasc:
        return 0
    
    else: 
        return -1



def dia_mes(mes_nasc, dia_nasc, mes_atual, dia_atual):
    if mes_nasc > mes_atual and dia_nasc > dia_atual:
        soma_dia = (dia_atual + 30) - dia_nasc

        soma_mes = ((mes_atual - 1) + 12) - mes_nasc
        return f'{soma_mes}/{soma_dia}'



main()






