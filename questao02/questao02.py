valor = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for n in notas:
    qtdnotas = int(valor / n)
    print("{} nota(s) de R$ {:.2f}".format(qtdnotas, n))
    valor -= qtdnotas * n

print("MOEDAS:")
for m in moedas:
    qtdmoedas = int(valor / m)
    print("{} moedas(s) de R$ {:.2f}".format(qtdmoedas, m))
    valor -= qtdmoedas * m
