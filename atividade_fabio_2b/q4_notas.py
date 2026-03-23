def main():

    nota_1 = obter_nota('Digite a primeira nota: ')
    nota_2 = obter_nota('Digite a segunda nota: ')

    resultado = calcular(nota_1, nota_2)

    print(resultado)













def obter_nota(descricao):
    numero = float(input(descricao))
    return numero






def calcular(nota1, nota2):
    
    
    media = (nota1 + nota2) / 2

    if media >= 7 and media <= 9.9:
        return 'Aprovado'
    
    elif media < 7 :
        return 'Reprovado'
    
    else :
        return 'Aprovado com distinção'
    




main()