# Создайте программу для игры в ""Крестики-нолики""


print('='*100)
print('\n')

desk = list(range(1,10))

def play_desk(desk):
    print('-'*12)
    for i in range(3):
        print('|', desk[0+i*3],'|', desk[1+i*3], '|', desk[2+i*3], '|')
        print('-'*12)

# play_desk(desk)

def choice(tic_tac):
    valid = False
    while not valid:
        player_index = input('Выберите клетку ' + tic_tac + ' --> ')
        try:
            player_index =int(player_index)
        except:
            print('Что-то пошло не так!!!')
            continue
        if player_index >= 1 and player_index <= 9:
            if(str(desk[player_index-1]) not in 'XO'):
                desk[player_index-1] = tic_tac
                valid = True
            else:
                print('Эта клетка уже занята! Выберите другую')
        else:
            print('Попробуй ещё')

def win_position(desk):
    victory = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in victory:
        if desk[i[0]] == desk[i[1]] == desk[i[2]]:
            return desk[i[0]]
    return False

def game(desk):
    count =0
    win = False
    while not win:
        play_desk(desk)
        if count % 2 == 0:
            choice('X')
        else:
            choice('0')
        count +=1
        if count > 4:
            player_win = win_position(desk)
            if player_win:
                print(player_win,'Победа')
                win = True
                break
            if count == 9:
                print('Для определения победителя нужена ещё одна игра')
        play_desk(desk)
game(desk)