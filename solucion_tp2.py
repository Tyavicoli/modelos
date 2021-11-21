import os

def ordenar_lista(minutos_lavado, dic_tiempos):
    result = []
    for i in minutos:
        result += dic_tiempos[i]
    return result

#Funcion que recibe un diccionario con las incompatibilidades, una lista de prendas y una nueva prenda 'b'.
#Devuelve True en caso de que la prenda 'b' sea incompatible por lo menos con 1 de las prendas de la lista
#Devuelve False si la prenda 'b' es compatible con todas las prendas de la lista
def son_incompatibles(dic_incomp, lista_a, b):
    for prenda in lista_a:
        if (str(b) in dic_incomp and str(prenda) not in dic_incomp[str(b)]) and (str(prenda) in dic_incomp and str(b) not in dic_incomp[str(prenda)]):
            continue
        else:
            return True
    return False


#Variables
incompatibles = {}
tiempos = {}
minutos =[]
resultado = {}
numero_lavado = 1
cantidad_prendas = 0
prendas_ordenadas_por_tiempo = []
indice = 0
lista_lavado = []

#Leo el enunciado
with open("/Users/tomas/OneDrive/Documentos/FIUBA/Modelos/enunciado_modelos_tp2.txt","r") as archivo:
    for linea in archivo:
        if linea[0] == 'c':
            continue
        aux = linea.split()
        if linea[0] == 'p':
            cantidad_prendas = int(aux[2])
        elif linea[0] == 'e':
            if aux[1] not in incompatibles:
                incompatibles[aux[1]] = [aux[2]]
            else:
                incompatibles[aux[1]].append(aux[2])
        elif linea[0] == 'n':
            if int(aux[2]) not in tiempos:
                minutos.append(int(aux[2]))
                tiempos[int(aux[2])] = [aux[1]]
            else:
                tiempos[int(aux[2])].append(aux[1])
    
    #Ordeno prendas por cantidad de minutos, primero las que tardan mas, ultimo las que tardan menos
    minutos.sort()
    prendas_ordenadas_por_tiempo = ordenar_lista(minutos, tiempos)
    
    
    while indice < cantidad_prendas:
        #Chequeo si la prenda esta en el resultado, si esta la salteo
        if prendas_ordenadas_por_tiempo[indice] in resultado:
            indice += 1
            continue
        #Si la prenda no esta en el resultado entonces empiezo a ver cual es la proxima prenda con tiempo mas cercano que no sea incompatible
        for i in range(indice, cantidad_prendas):
            #Chequeo si la otra prenda esta en el resultado
            if prendas_ordenadas_por_tiempo[i] in resultado or i == indice:
                continue
            #Me fijo si son compatibles
            if not son_incompatibles(incompatibles, [prendas_ordenadas_por_tiempo[indice]], prendas_ordenadas_por_tiempo[i]):
                lista_lavado.append(prendas_ordenadas_por_tiempo[indice])
                lista_lavado.append(prendas_ordenadas_por_tiempo[i])
                resultado[prendas_ordenadas_por_tiempo[indice]] = numero_lavado
                resultado[prendas_ordenadas_por_tiempo[i]] = numero_lavado
                #Me fijo que otras prendas son compatibles con las 2 que encontre como comptatibles
                for j in range(i, cantidad_prendas):
                    #Si la nueva prenda esta en resultado la saltea
                    if prendas_ordenadas_por_tiempo[j] in resultado:
                        continue
                    elif not son_incompatibles(incompatibles, lista_lavado, prendas_ordenadas_por_tiempo[j]):
                        lista_lavado.append(prendas_ordenadas_por_tiempo[j])
                        resultado[prendas_ordenadas_por_tiempo[j]] = numero_lavado
                lista_lavado = []
                numero_lavado += 1
                break
        indice += 1
    
    #Agrego a resultado las prendas que quedaron sueltas en lavados individuales
    for prenda in range(1, cantidad_prendas+1):
        if str(prenda) not in resultado:
            resultado[prenda] = numero_lavado
            numero_lavado += 1
            
    #Creo el archivo resultado
    file = open("/Users/tomas/OneDrive/Documentos/FIUBA/Modelos/resultado.txt", "w")
    for prenda in resultado.keys():
        file.write(str(prenda) + " " + str(resultado[prenda]) + "\n")
    file.close()