# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 00:00:30 2021

@author: tomas
"""
incompatibles = {}
tiempos = {}
resultado = {}
numero_lavado = 0
cantidad_prendas = 0

with open("/Users/tomas/OneDrive/Documentos/FIUBA/enunciado_modelos_tp1.txt","r") as archivo:
    for linea in archivo:
        if linea[0] == 'c':
            continue
        aux = linea.split()
        if linea[0] == 'p':
            cantidad_prendas = aux[2]
        if linea[0] == 'e':
            if aux[1] not in incompatibles:
                incompatibles[aux[1]] = [aux[2]]
            else:
                incompatibles[aux[1]].append(aux[2])
        if linea[0] == 'n':
            if aux[2] not in tiempos:
                tiempos[aux[2]] = [aux[1]]
            else:
                tiempos[aux[2]].append(aux[1])
    for n in tiempos.keys():
        for i in range(1, cantidad_prendas+1):
            
        print(n)
    print(tiempos)
    print(incompatibles)
    