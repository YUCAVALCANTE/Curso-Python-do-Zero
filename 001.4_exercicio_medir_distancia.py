import math

#ler linha com coordenadas
linha = input()

#separar linha e guardar em 2 variaveis
X1, Y1 = linha.split()

#Transformar em numeros inteiros
X1 =int(X1)
Y1 = int(Y1)

linha = input()

X2, Y2 = linha.split()

X2 =int(X2)
Y2 = int(Y2)

#distancia = raiz(x1-x2**2+(y1-y2)**2)

distancia = math.sqrt( (X1-X2)**2 + (Y1-Y2)**2 )
print(distancia)
