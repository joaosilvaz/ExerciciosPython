# Exercício 4)
peso = float(input("Informe o peso da pessoa em kg:"))
altura = float(input("Informe a altura da pessoa em metros:"))

print(type(peso))
print(type(altura))

imc = peso/(altura * altura)

print(f"O valor do imc é {imc}")
