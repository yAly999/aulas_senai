def calcular_media(nota1, nota2, nota3):
    soma = nota1 + nota2 + nota3
    media = soma/3
    return media

n1 = float(input("digite a primeira nota do aluno: "))
n2 = float(input("digite a segunda nota do aluno: "))
n3 = float(input("digite a terceira nota do aluno: "))

resultado = calcular_media(n1, n2, n3)
print(f"A media final é: {resultado}")