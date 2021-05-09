from functions import *
while True :
    add_user()
    quest = input(q)
    if quest == answ or quest == anws1 :
        del_it()
        add_user()
    else :
        add_user()
    quest1 = input(q1)
    if quest1 == answ or quest1 == anws1 :
        return_user()
    else :
        add_user()



#Ахмедов Амин