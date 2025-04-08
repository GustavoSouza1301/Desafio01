"""Dados:
entrada01: 3:45
entrada02: 14:20
saida: 6:05"""

hora01 = int(input("hora: "))
minutos01 = int(input("minutos: "))
hora02 = int(input("hora: "))
minutos02 = int(input("minutos: "))

minutoF = minutos01 + minutos02

if hora01 >12:
    valorH01 = hora01 - 12
else:
    valorH01 = hora01
if hora02 >12:
    valorH02 = hora02 - 12
else:
    valorH02 = hora02

horaF = valorH01 + valorH02

if minutoF >= 60:
    minutoF02 = minutoF - 60
    horaF02 = horaF + 1
    print(f"{horaF02}:{minutoF02}")
else:
    print(f"{horaF}:{minutoF}")