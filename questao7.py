numero=int(input('Digite um número: '))
fat=1
print("Fatorial = 1")
for n in range (2, (numero+1)):
    print(' x', n)
    fat=fat+n
print('Fatorial de ', numero, '=', fat)