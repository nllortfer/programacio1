import numpy as np
import matplotlib.pyplot as plt
import math
#np.dot(escalar)
#np.cross(vectorial)
#np.natmul(product matrius)
#np.linalg.det(determinant)
#np.linalg.inv(inversa)
#np.linalg.solve(resol un sistema en forma de matriu)
#np.linal.norm(modul)
#np.frompyfunc()
#ex1 
#a)
'''
a=np.arange(0,1.1,0.2)
print(a)
'''
#b)
'''
a=np.arange(1,10).reshape(3,3)
print (a)
'''
#c)
'''
a=np.arange(1,10).reshape(3,3)
a+=1
print (a)
'''
#d)
'''
a=np.identity(3)*2
print (a)
'''
'''
m1=[1,2,3]
m2=[4,5,6]
m3=np.add(m1,m2)
m3=np.sqrt(m1)
m3=np.sin(m1)
m3=np.abs(m1)
m3=np.round(m1,decimals=2)
'''
#transposada
'''
a=np.array([[1,2,3],[4,5,6]])
t1=a.T #no crea cap matriu, nomes se la mira
t2=a.T.copy()#la copia
a[0,0]=100
print (t1)
print (t2)
'''
'''
#concatenate
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[11,12,13],[14,15,16]])
c=np.concatenate((a,b),axis=0)#axis=>com vols concatenar les matrius
print (c)

#where
m=np.array([[1,2,3],[4,5,6]])
n=np.where(m%2==0,m*2,m*3)#(condicion, accion si la condicion se cumple, accion si no se cumple)
print (n)

#integral
#lx=np.arange(0,2*math.pi, .01)
lx=np.linspace(0,2*math.pi,628)#
ly=np.sin(lx)
plt.plot(lx,ly)
plt.show()
area=np.sum(ly*.01)
print (area)

a=np.array([[1,2,3],[4,5,6]])
print(np.ndarray.flatten(a))#aplana la matriu
    #[1 2 3 4 5 6]
for e in np.nditer(a): #per recorre una matriu
    print(e,end=' ')
    #1 2 3 4 5 6 

#acces indexat
v=np.array([1,2,3])
m=np.array([[1,2,3],[4,5,6]])
print(v[2])
print(m[1,2])
print(m[1])

a=np.arange(20)
m=np.array([np.arange(8),np.arange(7,-1,-1)]) #array: crea una  matriu
print (np.shape(a))  #(20,)
b=a.reshape((4,5))

c=np.linspace(10,20,5)
'''
