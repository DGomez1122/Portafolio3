#Diagonal de una Matriz
def DiagonalMatriz(matriz):
    if isinstance(matriz,list) and (matriz!=[]):
        if largo(matriz)==largo(matriz[0]):
            return AuxDiagonalMatriz(matriz,0,0,[])
        else:
            print("La matriz no es cuadrada")
    else:
        print("Error en parámetros de entrada")
def AuxDiagonalMatriz(matriz,contador,fila_actual,res):
    if matriz==[]:
        return res
    else:
        return AuxDiagonalMatriz(matriz,contador+1,fila_actual+1,res+[matriz[contador][fila_actual]])
