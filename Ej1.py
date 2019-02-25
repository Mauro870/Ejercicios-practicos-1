

def invertir_lista(unsort):
    mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string=list(unsort)
    string_inv=list(unsort)
    for i in range(len(string)-1,-1,-1):
        if string[i] in mayusculas:
            string[i]=string[i].lower()
        else:
            string[i]=string[i].upper()
        string_inv[(len(string)-1)-i]=string[i]
    return string_inv
unsort = input('Introduce una cadena de texto: ')
invertir_lista(unsort)
