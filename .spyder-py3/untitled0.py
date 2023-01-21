import numpy as np
import sympy as sym  # paquete para matematicas simbolicas
import matplotlib.pyplot as plt 

vectorx=np.array([0.473,np.pi/2,2.49, 3, 5, 50, 8])
vectorfx=np.array([0.455,1,0.606, 3, 6, 12, 23])
n=len(vectorx)

x=sym.Symbol('x') 
polinomio=0

for i in range(0,n,1):
    numerador=1
    denominador=1
    for j in range(0,n,1):
        if (i!=j):
            numerador=numerador*(x-vectorx[j])
            denominador=denominador*(vectorx[i]-vectorx[j])
        termino=(numerador/denominador)*vectorfx[i]
    polinomio=polinomio + termino
    
polix=sym.expand(polinomio)

# grafica
px=sym.lambdify(x,polinomio)
muestras=51
a=np.min(vectorx)
b=np.max(vectorx)
#xi=np.linspace(a,b,muestras)
xi=np.linspace(-5,5,100)
fi=px(xi)
plt.show()
plt.xlabel('eje x')
plt.ylabel('p(x)')
plt.title('polinomio de lagrange')
plt.grid()
plt.plot(vectorx,vectorfx,'o')# dibujamos los puntos
plt.plot(xi,fi)

print(polix)