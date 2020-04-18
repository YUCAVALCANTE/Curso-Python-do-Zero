# 4) Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5.


A =float(input("Insira a primeira nota do aluno: "))
B =float(input("Insira a segunda nota do aluno: "))
C =float(input("Insira a terceira nota do aluno: "))

peso1 = 2
peso2 = 3
peso3 = 5


mediap = ( (A * peso1) + (B * peso2) + (C * peso3) ) / (peso1 + peso2 + peso3)


print("O aluno possui a média ",mediap)