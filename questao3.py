escolha=int(input('Digite: 1 - Para médico ou advogado, 2 - Para professor ou jornalista, 3 - Para físico e 4 - Para comerciante'))
if escolha==1:
    salario=50
    if escolha==2:
        salario=24
        if escolha==3:
            salario=30
            if escolha==4:
                salario=12
else:
    salario=16

caminho=int(input('Escolha: 1 - Caminho A e 2 - Caminho B'))
if caminho==1:
    LucroA=int=(salario*20) + ((salario/2)*10)
    print('O seu lucro foi de : ',LucroA)
else:
    LucroB=int=(salario*20) + ((salario/2)*5)
    print('O seu lucro foi de: ',LucroB)