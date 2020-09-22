frase = input ("escreva a frase a ser transcrita \n")
frase_copy = frase
n = 0
p = 1



while (p == 1):    
    
    carac = input ("transcrever para * ou x?\n") 

    if (carac == "*" or carac == "x"):
        p = -44
        
    else:
        print("entrada nao valida")
        p = 1
        
if (p == -44):
    while (n < len(frase)):
        if (frase[n] != ' '):
            frase_copy = frase_copy.replace(frase[n], carac)
        n = n + 1

    print (frase_copy)
    


    
    


