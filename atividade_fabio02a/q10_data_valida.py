def main():

    ano = int(input('Digite o ano: '))
    mes = int(input('Digite o mês: '))
    dia = int(input('Digite o dia: '))

    if verificar_validade(ano, mes, dia):
        escrever('Essa data é válida')
    
    else:
        escrever('Essa data não é válida')








def verificar_validade(ano, mes, dia):
    if (ano >= 1 and ano <= 2026) and (mes >= 1 and mes <= 12) and (dia >= 1 and dia <= 30):
        return True
    else:
        return False
    


def escrever(conteudo):
    escrever = print(conteudo)
    return escrever



main()


















