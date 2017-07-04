print("===================================================")
equ = "Toda equação do segundo grau é do tipo ax^2 + bx + c = 0"
equ2 = "Então "
print(equ)
print(equ2)
a = int (input("Digite o valor de a: "))
b = int (input("Digite o valor de b: "))
c= int (input("Digite o valor de c: "))

delta = b**2 - 4*a*c

if delta > 0:
    print("A equação apresenta duas raízes reais e diferentes")
elif delta == 0:
    print("A equação apresenta uma raíz real")
else:
    print("A equação não possue raíz real")

print("===================================================")

lista = [1,2,3,4,5]
for n in lista:
    print(n)


