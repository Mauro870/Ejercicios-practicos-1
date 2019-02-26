def Diccionario_(unsort):
    aux=0
    trocado=1
    string=list(unsort)
# Se ordena el vector por el metodo de la burbuja
    while(trocado):
        trocado=0
        for char in range(len(string)-1):      
            if(string[char] > string[char+1]):
                aux=string[char]
                string[char]=string[char+1]
                string[char+1]=aux
                trocado +=1
# Se recorre el string eliminando elementos repetidos
    string_car=''
    if(string[0]!=string[1]):
        string_car += string[0]
    for i in range(len(string)-1):
        if(string[i]!=string[i+1]):
            string_car += string[i+1]   
# Borrado del diccionario
    diccionario={}
# Se cuentan las ocurrencias de cada caracter
    string_veces=''
    x=0
    for i in range(len(string_car)):
        for j in range(len(string)):
             if(string_car[i]==string[j]):
                x += 1
        string_veces += str(x) 
        diccionario.update({string_car[i]:str(x)})
        x=0
    print(string_car)
    print(string_veces)
    return diccionario    
unsort = input('Introduce una cadena de nùmeros: ')
Diccionario_(unsort)
