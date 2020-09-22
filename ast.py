frase = input ("escreva a frase a ser transcrita \n")
frase_copy = frase
p = 1

while (p == 1):    
    
    carac = input ("transcrever para * ou x?\n") 

    if (carac == "*"):
    	p = 0
    	
    elif (carac == "x"):
        p = 0
        carac = '×'
        
    else:
        print("entrada invalida, digite apenas x ou *")
        p = 1
        
    
for letra in frase:
   	
    if (letra == ' ' or letra == '?' or letra == '!' or letra == ',' or letra == '.' or letra == ";" or letra == ":"):
        continue
      
    else:
        frase_copy = frase_copy.replace(letra, carac)

print (frase_copy)
    

    
    


