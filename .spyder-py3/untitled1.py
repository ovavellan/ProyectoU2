# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 12:16:01 2022

@author: LENOVO
"""

import numpy
m=int(input('Valor de m:'))# introducir el numero de filas
n=int(input('Valor de n:'))# introducir el numero de columnas
A= numpy.zeros((m,n))# creo matriz vacia mxn
b = numpy.zeros((n))# vector b vacio
x=numpy.zeros((m))# vector x vacio
print ('Introduce la matriz de coeficientes y b como matriz aumentada')

# intrucir elementos de la matriz A y vector b
for r in range(0,m):
  for c in range(0,n):
    A[(r),(c)]=(input('Elemento a['+str(r+1)+','+str(c+1)+']=  '))
  b[(r)]=(input('Elemento b['+str(r+1)+']=  '))
  
#print(A)

print("")

#print(b)
  
# reduccion Gauss de la matriz   

for k in range(0,m):
    for r in range(k+1,m):
        factor=(A[r,k]/A[k,k])
        b[r]=b[r]-(factor*b[k])
        for c in range(0,n):
            A[r,c]= A[r,c]-(factor*A[k,c])

#sustitucion hacia atras

x[m-1]=b[m-1]/A[m-1,m-1]
print(x[m-1])
for r in range(m-2,-1,-1):
    suma=0
    for c in range(0,n):
        suma=suma+A[r,c]*x[c]
    x[r]=(b[r]-suma)/A[r,r]    


print("Resultado matriz")

print(A)

print('Resultado del vector')

print(x)