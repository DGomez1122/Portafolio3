#Sumar Filas

def largo(lista):
    if isinstance(lista,list):
        return largo_Aux(lista,0)
    else:
        return "Error"
def largo_Aux (lista, cont):
    if lista == []:
        return cont
    else:
        return largo_Aux (lista [1:], cont + 1)

def sumarFilas (matriz):
    if isinstance (matriz, list) and (matriz != []):
        return sumarFilas_aux (matriz, [])
    else:
        return "Error, el elemento de entrada no es válido"


def sumarFilas_aux (matriz, res):
    if matriz == []:
        return res
    else:
        sumas = suma_filas (matriz [0], 0)
        return sumarFilas_aux (matriz [1:], res + [sumas])


def suma_filas (lista, resultado):
    if lista == []:
        return resultado
    else:
        return suma_filas (lista [1:], resultado + lista [0])
