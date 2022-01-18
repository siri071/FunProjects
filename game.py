import random

def game(comp,you):
    if comp==you:
        return None
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp =='s':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("comp turn: Snake(s), Water(w), Gun(g)")
comp = random.randint(1,3)
if comp==1:
    retun = 'w'
elif comp==2:
    retun = 's'
else:
    retun = 'g'

you = input('your turn: chose anyone: ')
b=game(comp,you)

if b==None:
    print('game is tie!')
elif b:
    print('you win!')
else:
    print('you lose!')