# 4) Leia 2 valores de ponto flutuante A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5.

nota1 =float(input("Insira a primeira nota do aluno: "))
nota2 =float(input("Insira a segunda nota do aluno: "))

peso1 = 3.5
peso2 = 7.5


mediap = ( (nota1 * peso1) + (nota2 * peso2)  ) / (peso1 + peso2 )


print("O aluno possui a média ",mediap)