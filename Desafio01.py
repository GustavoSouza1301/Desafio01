hora01 = 3
minutos01 = 45
hora02 = 14
minutos02 = 20

horaF = hora01 + hora02
minutoF = minutos01 + minutos02

if hora01 >12:
    valorH01 = hora01 - 12

if hora02 >12:
    valorH02 = hora02 - 12
else:
    


else:
    if minutoF >= 60:
        horaF += 1
        minutoF2 = minutoF - 60
        print(f"{horaF}:{minutoF2}")

    else:
        print(f"{horaF}:{minutoF}")