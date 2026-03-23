def main():


    print('*** G - gasolina ***')
    print()
    print('*** A - Álcool ***')

    tipo = input('Digite o tipo: ')

    litros = float(input('Digite a quantidade de combustivel: '))

    resultado_gasolina = gasolina(litros)

    resultado_alcool = alcool(litros)





    if tipo == 'g' or tipo == 'G':
        print(resultado_gasolina)

    elif tipo == 'A' or tipo == 'a':
        print(resultado_alcool)

    else: 
        return 'Tipo não indentificado'











def gasolina(litro):
    if litro > 0 and litro <= 20:
        
        preco_litro1 = (2.50 - (2.50 * 0.03))

        calculo_litros1 = preco_litro1 * litro

        return f'{litro} litros de gasolina equivalem a {calculo_litros1}'
    
    elif litro > 20 :

        preco_litro2 = (2.50 - (2.50 * 0.05))

        calculo_litros2 = preco_litro2 * litro

        return f'{litro} litros de gasolina equivalem a {calculo_litros2}'
    
    else :
        return 'Valor inválido'



def alcool(litro):
    if litro > 0 and litro <= 20 :
        
        preco_litro1 = 1.90 - (1.9 * 0.04)

        calculo_litros1 = preco_litro1 * litro

        return f'{litro} litros de álcool equivalem a {calculo_litros1}'
    
    
    
    elif litro > 20:

        preco_litro2 = 1.90 - (1.90 * 0.06)

        calculo_litros2 = preco_litro2 * litro
        
        return f'{litro} litros de álcool equivalem a {calculo_litros2}'
    
    else:
        return 'Valor inválido'



main()