import random

esqueleto=random.randrange(20, 51)
corcunda=random.randrange(20, 51)
ortodontista=random.randrange(20, 51)
aparelho=random.randrange(20, 51)
mulher=random.randrange(20, 51)
fquarteto=esqueleto+corcunda+ortodontista+aparelho+mulher
senhora=random.randrange(20, 51)
musculacao=random.randrange(20, 51)
fdupla=senhora+musculacao
if fquarteto>fdupla+120:
    print('O portão abriu!')
else:
    print('O portão não abriu!')