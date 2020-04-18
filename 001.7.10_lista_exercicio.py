
#10) Faça um programa que leia a quantidade de dias, horas, minutos e segundos. Calcule o total em segundos.

dia = int(input("Quantos dias? "))
hora = int(input("Quantas horas? "))
minut = int(input("Quantos minutos? "))
sec = int(input("Quantos segundos? "))

print(f"O total, em segundos é: {sec + minut*60 + hora*3600 + dia*86400}")