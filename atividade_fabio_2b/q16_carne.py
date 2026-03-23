def main():
    print('***Tabela carne***')
    print()
    print('** F - file')
    print('** A - alcatra')
    print('** P - picanha')

    

    tipo = input('Digite a letra da carne desejada: ')
    quantidade_kg = float(input('Digite a quantidade desejada: '))

    cartao = input('Vai usar cartão tabajara? ')
    
    
    preco_file = file_preco(quantidade_kg)

    preco_alcatra = alcatra_preco(quantidade_kg)

    preco_picanha = picanha_preco(quantidade_kg)


    if cartao == 'sim' or cartao == 'SIM' or cartao == 'Sim':
        
        
        if tipo == 'f' or tipo == 'F':

            desconto = preco_file * 0.10
            valor_pagar = preco_file - desconto

            print('Tipo: file')
            print(f'Quantidade: {quantidade_kg}kg')
            print(F'Preço total: {preco_file}')
            print(f'Tipo de pagamento: CARTÂO TABAJARA')
            print(f'desconto de 10%: {desconto}')
            print(f'Preço a pagar: {valor_pagar}')


        elif tipo == 'a' or tipo == 'A':

            desconto2 = preco_alcatra * 0.10
            valor_pagar2 = preco_alcatra - desconto2

            print('Tipo: Alcatra')
            print(f'Quantidade: {quantidade_kg}kg')
            print(F'Preço total: {preco_alcatra}')
            print(f'Tipo de pagamento: CARTÂO TABAJARA')
            print(f'desconto de 10%: {desconto2}')
            print(f'Preço a pagar: {valor_pagar2}')


        elif tipo == 'p' or tipo == 'P':

            desconto3 = preco_picanha * 0.10
            valor_pagar3 = preco_picanha - desconto3

            print('Tipo: Picanha')
            print(f'Quantidade: {quantidade_kg}kg')
            print(F'Preço total: {preco_picanha}')
            print(f'Tipo de pagamento: CARTÂO TABAJARA')
            print(f'desconto de 10%: {desconto3}')
            print(f'Preço a pagar: {valor_pagar3}')

        else :
            print('Por favor digite a letra de acordo com a tabela')
    

    
    elif cartao == 'não' or cartao == 'NÃO' or cartao == 'Não' or cartao == 'nao':

        if tipo == 'f' or tipo == 'F':

            
            valor_pagar = preco_file

            print('Tipo: file')
            print(f'Quantidade: {quantidade_kg}kg')
            print(F'Preço total: {preco_file}')
            print(f'Tipo de pagamento: Dinheiro físico')
            print(f'Preço a pagar: {valor_pagar}')


        elif tipo == 'a' or tipo == 'A':

           
            valor_pagar2 = preco_alcatra 

            print('Tipo: Alcatra')
            print(f'Quantidade: {quantidade_kg}kg')
            print(F'Preço total: {preco_alcatra}')
            print(f'Tipo de pagamento: Dinherio físico')
            print(f'Preço a pagar: {valor_pagar2}')


        elif tipo == 'p' or tipo == 'P':

            
            valor_pagar3 = preco_picanha

            print('Tipo: Picanha')
            print(f'Quantidade: {quantidade_kg}kg')
            print(F'Preço total: {preco_picanha}')
            print(f'Tipo de pagamento: Dinheiro físico')
            print(f'Preço a pagar: {valor_pagar3}')

        else:
            
            print('Por favor digite a letra de acordo com a tabela')

    else :
        print('Digite somente: "sim" ou "não')
        





def file_preco(kg):
    if kg > 0 and kg <= 5:
        preco1 = kg * 4.90
        return preco1
    
    elif kg > 5:
        preco2 = kg * 5.80

        return  preco2
    

def alcatra_preco(kg):
    if kg > 0 and kg <= 5:
        preco1 = kg * 5.90

        return preco1
    
    elif kg > 5:
        preco2 = kg * 6.80

        return preco2





def picanha_preco(kg):
    if kg > 0 and kg <= 5:
        preco1 = kg * 6.90

        return preco1
    
    elif kg > 5:
        preco2 = kg * 7.80
        
        return preco2


main()