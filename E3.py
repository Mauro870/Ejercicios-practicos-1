def invertir_string(unsort):
    especial = '|@#~€¬{}[]()\!"·$%&=?¿,.;*@ł¶+-º/ª><¡'
    string= unsort
    string_especial=''
    string_normal=''
    string_inv=''
    string_total=''
    posicion_e=''
    posicion_n=''
    
    for i in range(len(string)):
        if string[i] in especial:
            string_especial += string[i]
            posicion_e += str(i)
        else:
            string_normal += string[i]
            posicion_n += str(i)
            
    for i in range(len(string_normal)-1,-1,-1):
        string_inv += string_normal[i]
    string_total= list(string_inv + string_especial)
    
    for i in range(len(string_normal)):
        dato=int(posicion_n[i])
        string_total[dato] = string_inv[i]
        
    for i in range(len(string_especial)):
        dato=int(posicion_e[i])
        string_total[dato] = string_especial[i]
        
    return string_total
unsort = input('Introduce una cadena de texto: ')
invertir_string(unsort)
