failas = open('./info.txt', encoding="utf8")
nuskaitytas_tekstas = failas.read()
print(nuskaitytas_tekstas)
failas.close()

print("labas",end="\n")
print("labas",end="")
print("labas",end="\n")


with open('./info.txt') as failas:
    visas_tekstas = failas.readlines()
    print(visas_tekstas)
    # print(len(visas_tekstas))

with open('./info.txt', 'a') as failas:
    failas.write('pirma\n')
    failas.write('antra\n')
    failas.write('trecia\n')
    failas.write('ketvirta\n')


# with open('./rasymui5.txt', 'w') as failas:
#     failas.write('labas krabas\n')

# with open('./rasymui5.txt', 'a') as failas:
#     failas.write('daugiau teksto\n')
#     failas.write('failo papildymas')
#
with open('./rasymui5.txt', 'r+') as failas:
    failas.write('ar atsiras failo virsuje?\n')