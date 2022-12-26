# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021(или сколько вы скажете) конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28(или сколько вы зададите в начале) конфет. Все конфеты оппонента достаются сделавшему последний ход. Сделайте эту игру.
# 
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# 
# Если делаете a и b - не нужно создавать отдельных файлов с полностью копированным кодом, лучше выделите в отдельные функции бота и умного бота.


from random import randint

def input_data(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, что-то пошло не так! Введите верное количество конфет: "))
    return x


def player_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. На столе осталось {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # очерёдность

if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

count_1 = 0 
count_2 = 0

while value > 28:
    if flag:
        k = input_data(player1)
        count_1 += k
        value -= k
        flag = False
        player_print(player1, k, count_1, value)
    else:
        k = input_data(player2)
        count_2 += k
        value -= k
        flag = True
        player_print(player2, k, count_2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")