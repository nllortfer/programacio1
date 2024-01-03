import math
import matplotlib.pyplot
import numpy as np

num_files=int(input('? '))#files
num_colum=int(input('? '))#columnas
f=[]#llista magatzem incompleta(sense elevador)
e=[]#llista elevador
separacion=[]#palo

for i in range(num_colum): #concatena la lista del elevador con el numero de filas
   e.append('_') 
   
for i in range (num_files): #completa el magatzem
    f.append(e)
    
for i in range(num_colum):  #crea separacion visual
    separacion.append('|')
   
elev=np.array(e) #lista e convertida en matriz(elevador)
elev=elev.reshape(num_colum,1)  #convierte en matriz mx1
separacion=np.array(separacion) #Convierte la lista de los palos en una matriz
separacion=separacion.reshape(num_colum,1) #Convierte la separacion(visual) en mx1

matriz= np.hstack([elev,separacion,f]) #concatenació de les matrius(elevador,magatzem)

for fila in matriz: #visualmente (palos/comas/claudators)
    print('|',*fila,'|')
