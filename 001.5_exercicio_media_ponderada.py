#Desafio: Leia 3 valores de ponto flutuante, um em cada linha. Depois, calcule a média ponderada desses valores. O primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro tem peso 5.

#entrar com 3 números
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

# calcule a media ponderada O primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro tem peso 5.
peso1 = 2
peso2 = 3
peso3 = 5

mediap = ( (a * peso1) + (b * peso2) + (c* peso3) ) / (peso1 + peso2 + peso3)

#imprimir a media
print (mediap) 


