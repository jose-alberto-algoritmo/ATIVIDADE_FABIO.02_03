def main():

    numero = int(input("Digite o número: "))

    
    
    
    
    if par_impar(numero):
        escrever('Esse número é par')
        
    else:
        escrever('esse número é impar')






def escrever(conteudo):
    escrever = print(conteudo)




def par_impar(numero):
    if (numero % 2) == 0:
        return True
    else:
        return False
    

main()