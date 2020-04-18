# 3) Faça um programa que peça 2 números inteiros e 1 número real. Calcule e mostre:
# a) O produto do dobro do primeiro com metade do segundo.
# b) A soma do triplo do primeiro com o terceiro.
# c) O terceiro elevado ao cubo.


n1 =int(input("Insira o 1º numero Inteiro: "))
n2 =int(input("Insira o 2º numero Inteiro: "))
n3 =float(input("Insira o 3º numero Real: "))


a = (n1*2)+(n2/2)
a2 = (n1*3)+n3
a3 = n3 ** 3

print("O produto do dobro do primeiro com metade do segundo será: ", a)
print("A soma do triplo do primeiro com o terceiro será: ", a2)
print("O terceiro elevado ao cubo será :", a3)