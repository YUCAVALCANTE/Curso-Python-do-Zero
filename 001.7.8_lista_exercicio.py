

#FFaça um programa que converta a temperatura digitada em Celsius para Fahrenheit.
# Cálculo para Fahrenheit: F = 9*C/5+32

# Modificando o exercício anterior, faça um programa que converta a temperatura digitada em Fahrenheit para Celsius


Fahrenheit = float(input("Insira o valor em Fahrenheit a ser convertido: "))

Celsius = (Fahrenheit - 32)*5/9

print(f"{Fahrenheit} Fahrenheit será {Celsius} Celsius.")