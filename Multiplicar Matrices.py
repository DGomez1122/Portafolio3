#Multiplicar Matrices.

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


def multiplicarMatrices(matriz, matriz2):
    if isinstance(matriz, list) and (matriz != []) and isinstance(matriz2, list) and (matriz2 != []):
        if largo(matriz[0]) != largo(matriz2):
            return "Error, orden no adecuado"
        else:
            return multiplicarMatrices_aux(matriz, matriz2, 0, [])
    else:
        return "Error, los elemento de entrada deben ser listas y no deben estar vacías"


def multiplicarMatrices_aux(matriz, matriz2, cont, res):
    if cont == largo(matriz):
        return res
    else:
        res += [multiplicarFilaMatriz(matriz[cont], matriz2)]
        return multiplicarMatrices_aux(matriz, matriz2, cont + 1, res)


def obtenerColumna(matriz, indice, conti):
    if conti == largo(matriz):
        return []
    else:
        return [matriz[conti][indice]] + obtenerColumna(matriz, indice, conti + 1)


def multiplicarFilaColumna(i, j, cont):
    if cont == largo(i) and cont == largo(j):
        return 0
    else:
        return i[cont] * j[cont] + multiplicarFilaColumna(i, j, cont + 1)


def multiplicarFilaMatriz(i, matriz):
    return multiplicarFilaMatriz_aux(i, matriz, 0, largo(matriz[0]), [])


def multiplicarFilaMatriz_aux(i, matriz, j_actual, j_total, res):
    if j_actual == j_total:
        return res
    else:
        j = obtenerColumna(matriz, j_actual, 0)
        res += [multiplicarFilaColumna(i, j, 0)]
        return multiplicarFilaMatriz_aux(i, matriz, j_actual + 1, j_total, res)
