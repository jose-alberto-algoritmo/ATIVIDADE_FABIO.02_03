def main():

    horas = int(input('Digite a quantidade de horas: '))

    valor = float(input('Digite a o valor da hora: '))

    salario_bruto = valor * horas

    descontos_imposto = descontos_ir(salario_bruto)
    desconto_inss = inss_desconto(salario_bruto)
    desconto_fgts = fgts_desconto(salario_bruto)


    desconto_total = descontos_imposto + desconto_inss

    salario_liquido = salario_bruto - desconto_total






    print(f'Salário bruto: {salario_bruto}')
    print(f'Imposto de renda: {descontos_ir(salario_bruto)}')
    print(f'INSS: {inss_desconto(salario_bruto)}')
    print(f'FGTS: {fgts_desconto(salario_bruto)}')
    print(f'Desconto total: {desconto_total}')
    print(f'salário liquido: {salario_liquido}')
















def descontos_ir(salario):

    if salario <= 900:
        descont1 = 0
        return descont1
    
    elif salario > 900 and salario <= 1500:
        desconto2 = salario * 0.05
        return desconto2
    
    elif salario > 1500 and salario <= 2500:
        desconto3 = salario * 0.10
        return desconto3
    
    else:
        desconto4 = salario * 0.20
        return desconto4




def sindicato_desconto(salario):
    desconto = salario * 0.03
    return desconto




def inss_desconto(salario):
    desconto = salario * 0.10
    return desconto



def fgts_desconto(salario):
    desconto = salario * 0.11
    return desconto


main()