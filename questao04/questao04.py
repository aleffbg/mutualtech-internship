var = [int(i) for i in input().split()]
horainicial = var[0]
mininicial = var[1]
horafinal = var[2]
minfinal = var[3]

horatotal = horafinal - horainicial

if horatotal < 0:
    horatotal += 24
mintotal = minfinal - mininicial

if mintotal < 0:
    mintotal += 60
    horatotal -= 1

if mintotal == 0 and horatotal == 0:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horatotal, mintotal))
