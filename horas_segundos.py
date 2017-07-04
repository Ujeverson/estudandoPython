seg = int(input("Digite o número de segundos que quer converter: "))


horas = seg //3600
segundosRestantes = seg%3600
minutos = segundosRestantes // 60
segundos = segundosRestantes%60


print(seg, "é igual a: ", horas,"h", minutos,"min", segundos, "s")
