import math

print("Calculadora de Equação de Segundo Grau!")

# entradas
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# calcula o Δ
Δ = b ** 2 - 4 * a * c

print("O valor de Δ é", Δ)

if (Δ < 0):
    print("Para -Δ não existem raízes reais!")
else:
    if (Δ == 0):
        x = (-b + math.sqrt(Δ)) / (2 * a)
        print("Para Δ = 0 temos duas raízes iguais com valor", x)
    else:
        x1 = (-b + math.sqrt(Δ)) / (2 * a)
        x2 = (-b - math.sqrt(Δ)) / (2 * a)
        print("Para Δ positivo temos duas raízes diferentes!")
        print("x¹ =", x1)
        print("x² =", x2)