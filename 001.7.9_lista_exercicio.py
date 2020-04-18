#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem de aumento. Mostre o valor do aumento e do novo salário.

salario = float(input("Qual o valor do salário? R$ "))
porcentagem = float(input("Qual a porcentagem de aumento? %"))

aumento = salario * porcentagem/100
valorfinal = salario + aumento

print(f"O aumento será de R$ {aumento} , sendo assim o salário reajustado será de R$ {valorfinal}")