#1) Faça um programa que leia dois números e calcule:
    #a) A soma.
    #b) A subtração.
    #c) A multiplicação.
    #d) A divisão.
    #e) A exponenciação.
    #f) O módulo.
    #g) O resto.

#entrar com 2 números
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

# letra a
soma = n1 + n2
print(f"Resultado da letra a: {soma}")

# letra b
subtração = n1 - n2
print(f"Resultado da letra b: {subtração}")

# letra c
multiplicação = n1 * n2
print(f"Resultado da letra c: {multiplicação}")

# letra d
divisão = n1 / n2
print(f"Resultado da letra d: {divisão}")

# letra e
exponenciação = n1 ** n2
print(f"Resultado da letra e: {exponenciação}")

# letra f e g
modulo = n1 % n2
print(f"Resultado da letra e e g: {modulo}")

