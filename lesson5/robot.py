import math
from os import system


x=0
y=0
com=[0,0]
while len(com) != 0 and len(com) < 3:
    com.clear
    com=input("\nКуда направляться роботу?\nДля этого следуйте инструкции:\nU=вверх, D=вниз, L=влево, R=вправо + кол-во шагов\nВведите инструкцию:").split()
    if len(com) == 0:
        print("\n\nПрограмма завершена")
        r = math.sqrt((x ** 2) + (y ** 2))
        print(f"Расстояние равно: {r}")
        break 
    com[1]=int(com[1])
    if com[0]=="U":
        y=y+com[1]
    elif com[0]=="D":
        y=y-com[1]
    elif com[0]=="L":
        x=x-com[1]
    elif com[0]=="R":
        x=x+com[1]
    else:
        system('cls')
        print("\nОшибка ввода!")



