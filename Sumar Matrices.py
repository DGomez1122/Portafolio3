#Suma Matrices

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

def sumaMatrices (matriz, matriz2):
    if matriz == [] and matriz2 == []:
        return []
    elif largo(matriz) != largo(matriz2):
        return "Error, la cantidad de los elementos debe ser igual"
    else:
        return sumaMatrices_aux(matriz, matriz2, 0, [])


def sumaMatrices_aux(matriz, matriz2, cont_i, res):
    if cont_i == largo(matriz):
        return res
    else:
        suma = suma_matrices(matriz[cont_i], matriz2[cont_i], 0)
        return sumaMatrices_aux(matriz, matriz2, cont_i + 1, res + [suma])


def suma_matrices(lista_1, lista_2, cont_j):
    if cont_j == largo(lista_1):
        return []
    else:
        return [lista_1 [cont_j] - lista_2 [cont_j]] + suma_matrices(lista_1, lista_2, cont_j + 1) 
