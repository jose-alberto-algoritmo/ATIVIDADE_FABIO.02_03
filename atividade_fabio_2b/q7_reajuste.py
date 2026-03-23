def main():
    salario = float(input('Digite o valor do salário: '))

    resulatodo = reajuste(salario)

    print(resulatodo)










def reajuste(salario):
    if salario > 0 :
        
        if salario <= 280:
            aumento1 = salario * 0.20
        
            salario_atual1 = aumento1  + salario

            return f'O salário {salario}R$ teve um aumento de 20%({aumento1}), que é igual a {salario_atual1}'
    

    
        elif salario > 280 and salario < 700:
             aumento2 = salario * 0.15
        
             salario_atual2 = aumento2 + salario

             return f'O salário {salario}R$ teve um aumento de 15%({aumento2}), que é igual a {salario_atual2}'
    
    
        elif salario >= 700 and salario <= 1500:
             aumento3 = salario * 0.10

             salario_atual3 = aumento3 + salario
        
             return f'O salário {salario}R$ teve um aumento de 10%({aumento3}), que é igual a {salario_atual3}'
    
        else :
             aumento4 = salario * 0.05

             salario_atual4 = aumento4 + salario

             return f'O salário {salario}R$ teve um aumento de 5%({aumento4}), que é igual a {salario_atual4}'

    else:
        return "salário inválido"

main()