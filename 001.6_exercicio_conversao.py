#Dado um valor de tempo em segundos (inteiro), converta-o para o formato horas:minutos:segundos

#Digite total do tempo

t = int(input("Digite o tempo em segundos: "))

#1 hora = possui 3600s / 1 minuto possui 60s 

hora = t // 3600
minuto = (t % 3600) // 60
seg = t % 60
print(f"O tempo digitado, em horas, será: {hora}:{minuto}:{seg}")