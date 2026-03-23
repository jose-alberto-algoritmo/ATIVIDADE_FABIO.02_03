def main():
    horas_prof1 = int( input("Digite a quantidade de horas do professor1: "))
    
    valor_prof1 = float(input('Digite a valor em reais ganho por horas pelo professor1: '))
    
    horas_prof2 = int( input('Digite a quantidade de horas do professer2: '))

    valor_prof2 = float(input('Digite a valor em reais ganho por horas pelo professor2:  '))



    salario_prof1 = salario(horas_prof1, valor_prof1)

    salario_prof2 = salario(horas_prof2, valor_prof2)


    maior_sala = maior(salario_prof1, salario_prof2)

    print(f'O salário do professor1 é de {salario_prof1}')

    print(f'O salário do professor2 é de {salario_prof2}')

    print(maior_sala)







def salario(hora, valor):
    salario = hora * valor
    return salario



def maior(s1, s2):
    if s1 > s2:
        return f'O salário do professor1 é maior que o salário do professor2'
    elif s2 > s1:
        return f'O salário do professor2 é maior que o salário do professor1'
    else:
        return f'O salário do dois professores são iguais'
    


main()