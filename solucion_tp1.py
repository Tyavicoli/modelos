import os

def ordenar_lista(minutos_lavado, dic_tiempos):
    result = []
    for i in minutos:
        result += dic_tiempos[i]
    return result

def son_incompatibles(dic_incomp, a, b):
    if a not in dic_incomp[b]:
        return False
    return True




incompatibles = {}
tiempos = {}
minutos =[]
resultado = {}
numero_lavado = 1
cantidad_prendas = 0
prendas_ordenadas_por_tiempo = []
indice = 0

with open("/Users/tomas/OneDrive/Documentos/FIUBA/Modelos/enunciado_modelos_tp1.txt","r") as archivo:
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
    #for n in tiempos.keys():
        #for i in range(1, cantidad_prendas+1):
    minutos.sort(reverse=True)
    prendas_ordenadas_por_tiempo = ordenar_lista(minutos, tiempos)
    
    
    while indice < cantidad_prendas:
        if prendas_ordenadas_por_tiempo[indice] in resultado:
            indice +=1
            continue
        for i in range(indice + 1, cantidad_prendas):
            if prendas_ordenadas_por_tiempo[i] in resultado:
                continue
            if not son_incompatibles(incompatibles, prendas_ordenadas_por_tiempo[indice], prendas_ordenadas_por_tiempo[i]):
                resultado[prendas_ordenadas_por_tiempo[indice]] = numero_lavado
                resultado[prendas_ordenadas_por_tiempo[i]] = numero_lavado
                numero_lavado += 1
                break
        indice += 1
    
    for prenda in range(1, cantidad_prendas+1):
        if str(prenda) not in resultado:
            resultado[prenda] = numero_lavado
            numero_lavado += 1
    
    file = open("/Users/tomas/OneDrive/Documentos/FIUBA/Modelos/resultado.txt", "w")
    for prenda in resultado.keys():
        file.write(str(prenda) + " " + str(resultado[prenda]) + "\n")
    file.close()