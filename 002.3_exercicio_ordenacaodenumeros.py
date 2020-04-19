#   Serão dados 3 números inteiros, todos na mesma linha. Imprima na tela os números em ordem crescente, um em cada linha.
#   Exemplo
#   ​7 21 3
#   Saída
#   3
#   7
#   21

#entrada dos números:

num1, num2, num3 = input("Digite 3 números separados por espaço --> __ __ __: ").split()

#transformando para n inteiro
num1 = int(num1)    
num2 = int(num2)
num3 = int(num3)

# escolhendo a ordem  

if num1 < num2 > num3:
    if num1 < num3:
        print(f"Ordem crescente: {num1}\n{num3}\n{num2}")
    else:
        print(f"Ordem crescente: {num3}\n{num1}\n{num2}")
elif num1 < num3 > num2:
    if num1 < num3:
        print(f"Ordem crescente: {num1}\n{num2}\n{num3}")
    else:
        print(f"Ordem crescente: {num2}\n{num1}\n{num3}")
else:
    if num2 < num3:
        print(f"Ordem crescente: {num2}\n{num3}\n{num1}")
    else:
        print(f"Ordem crescente: {num3}\n{num2}\n{num1}")   


