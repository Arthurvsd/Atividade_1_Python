opcao=int(input('Escolha entre: 1 - Para pés no chão, 2 - Para Usar botas e 3 - Para sair no burro'))
if opcao==1:
    tempo=50
elif opcao==2:
    tempo=40
elif opcao==3:
    tempo=30

opcao=int(input('Escolha entre: 1 - Nadar no rio ou 2 - Não entrar no rio'))
if opcao==1:
    tempo=40

opcao=int(input('Escolha entre: 1 - Comer goiabas ou 2 - Não comer'))
if opcao==1:
    tempo=tempo+20

opcao=int(input('Escolha: 1 - Trocar ptialinas ou 2 - Não trocar'))
if opcao==1:
    quantidade=int(input('Quantas foram? '))
    tempo=tempo+10
opcao=int(input('Escolha: 1 - Chico encontrou a onça ou 2 - Não a encontrou'))
if opcao==1:
    tempo=tempo-30
print('Chico levou: ',tempo,'de tempo para chegar na escola!')


