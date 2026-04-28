def criar_perfil(nome, idade, cidade):
    print(f"nome: {nome}, idade: {idade}, cidade: {cidade}")

criar_perfil(nome = "alysson", idade = 18, cidade = "curitiba" )

def somar_tudo(*numeros):
    return sum(numeros)

somar_tudo(1, 2)
somar_tudo(1, 2, 3)
somar_tudo(1, 2, 5, 6)

