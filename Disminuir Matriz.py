#Disminuir Matriz
def disminuirMatriz(matriz):
    if isinstance(matriz,list) and (matriz!=[]):
        if len(matriz[0])==len(matriz):
            return imparesMatriz(matriz)
        else:
            print("Error en tamaño de la matriz, debe ser cuadrada")
    else:
        print("Error en parámetros de entrada")
def imparesMatriz(matriz):
    res=[]
    i=0
    j=0
    while i<len(matriz):
        while j<len(matriz[0]):
            if matriz[i][j]%2!=0:
                pos=matriz[i][j]
                res+=[pos]
                j+=1
            elif matriz[i][j]%2==0:
                j+=1
            else:
                pos=matriz[i][j]
                res+=[pos]
                j+=1
        j=0
        i+=1
    return res
