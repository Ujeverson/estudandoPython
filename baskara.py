import math

nome = input("Digite seu nome: ")

print(nome, ", você já conhece uma equação de 2º grau.")
print(" ")
print("Agora você só precisa digitar os valores dos coeficiente a, b e c, da equação.")
print("-"*20)
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c
print("O valor de delta é: ", delta)
print("="*30)
x1 = (-b + math.sqrt(delta))/(2 * a)
x2 = (-b - math.sqrt(delta))/(2 * a)

if delta < 0:
    print("A equação não possui raizes reais, pois delta tem valor igual a ", delta)
elif delta == 0:
    print("A equação possui duas raizes reais e iguais. x'=x'' {:.3f}".format(x1))
else:
    print("A equação poussui duas raizes reais e diferentes. x'= {:.3f} e x''={:.3f}".format(x1, x2))
