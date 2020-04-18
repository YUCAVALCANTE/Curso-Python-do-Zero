#Faça um programa que peça 4 notas bimestrais e mostre a média. 

#entrar com 2 números
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

# calcule a media
media = (n1+n2+n3+n4) / 4

#imprimir a media
print(f"A media das notas será: {media}")