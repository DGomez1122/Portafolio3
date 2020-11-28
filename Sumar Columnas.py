#Sumar Columnas.

def largo(lista):
    if isinstance(lista,list):
        return largo_Aux(lista,0)
    else:
        return "Error"
def largo_Aux(lista, cont):
    if lista == []:
        return cont
    else:
        return largo_Aux(lista [1:], cont+ 1)

        
def sumar_columnas (matriz):
    if isinstance (matriz, list) and (matriz != []):
        return sumar_columnas_aux (matriz, 0, 0, 0, [])
    else:
        return "Error, el elemento de entrada es inválido"

    
def sumar_columnas_aux (matriz, cont_f, cont_c, suma_col, resultado):
    if cont_c == largomatriz [0], 0):
        return resultado
    if cont_f == largo(matriz, 0):
        return sumar_columnas_aux (matriz, 0, cont_c + 1, 0, resultado + [suma_col])
    else:
        suma_col += matriz[cont_f][cont_c]
        return sumar_columnas_aux (matriz, cont_f + 1, cont_c, suma_col, resultado)
