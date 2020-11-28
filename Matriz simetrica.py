#Matriz Simétirca
#No funciona del todo
def matrizSimetrica(matriz):
    if isinstance(matriz,list) and (matriz!=[]):
        if len(matriz)==len(matriz[0]):
            return AuxSimetrica(matriz)
        else:
            print("La matriz no es cuadrada")
    else:
        print("Error en parámetros de entrada")
def AuxSimetrica(matriz):
    if matriz==transpuesta(matriz):
        return ("Sime")
    elif matriz!=transpuesta(matriz):
        return ("anti")
                             
#transpuesta    
def transpuesta(matriz):
    if isinstance (matriz,list) and (matriz!=[]):
        if largo(matriz)==largo(matriz[0]):
            return AuxTranspuesta(matriz,0,0,[],[])
        else:
            print("Error la matriz no es cuadrada")
    else:
        print("Error en parámetros de entrada, intente cambiarlos")


def AuxTranspuesta(m,cont_i,cont_j,lista_temp,res):
    if cont_i==largo(m):
        return AuxTranspuesta(m,0,cont_j+1,[],res+[lista_temp])
    if cont_j==largo(m[0]):
        return res
    else:
        if m[cont_i][cont_j]:
            return AuxTranspuesta(m,cont_i+1,cont_j,lista_temp+[m[cont_i][cont_j]],res)
        else:
            print("Error en parámetros")
