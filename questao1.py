notapt=float(input('Qual a sua nota em Português? '))
if notapt>=8:
    notamt=float(input('Qual a sua nota em Matemática? '))
    if notamt>7:
        notapd=int(input('Qual a sua nota no teste de poder? '))
        if notapd==10:
            print('Ômega')
        else:
            escolha=int(input('Se você for telepata digite 1!'))
            if escolha==1:
                print('Sua média é: ',notapt+notamt+(notapd*2)/4)
            else:
                print('Sua média é: ',notapt+notamt+notapd/3)
    else:
        print('Reprovou em Matemática!')
else:
    print('Reprovou em Português!')                    

   
                  
