# -- coding: utf-8 --
"""
Created on Fri Dec 31 18:39:34 2021

@author: PERSONAL
"""
# cargamos librerias necesarias
import numpy as np
import sympy as sym  # paquete para matematicas simbolicas
import matplotlib.pyplot as plt 

vectorx=np.array([[0.473],[1.57],[2.49]])
#x=np.array([1,0,-3])
vectorfx=np.array([[0.455],[1],[0.606]])
n=len(vectorx)
matriz = np.zeros((n,n-1))
total= np.concatenate((vectorfx,matriz), axis=1)
total= np.concatenate((vectorx,total), axis=1)

for i in range(1,n,1):
    for j in range(2,n+1,1):
        if j-i<2:
            total[i][j]=((total[i,j-1]-total[i-1,j-1])/(total[i,0]-total[i-(j-1),0]))
        else:
            total[i][j]=0
x=sym.Symbol('x') 
       
polix=total[0,1]
#or i in range(0,n-1,1):
factor=1
for j in range(0,n-1,1):
    factor=factor*(x-total[j,0])
    termino=total[j+1,j+2]
    polix=polix+termino*factor
    
#realizamos las operaciones del polinomio
polix=polix.expand()
#pra graficar el polinomio
px=sym.lambdify(x,polix)

# defino valores x
varx=np.linspace(-5,5,100)
# evaluamos el polinomio en dichos valores
vary=px(varx)
plt.plot(varx,vary)
plt.scatter(vectorx,vectorfx)
print(polix)