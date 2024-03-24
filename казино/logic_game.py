from random import randint
from decouple import config


list_slot = randint(1, 30)
game_over = True
my_money = config('MY_MONEY', default=1000, cast=int)

class Game:

    def input_money(self):
        global my_money
        while True:
            try:
                bet_money = int(input(f'Ваш баланс: {my_money}$.\nВведите сумму ставки: '))

                if bet_money > my_money:
                    print('У вас недостаточно денег для этой ставки.')
                elif bet_money <= 0:
                    print('Введите положительную сумму.')
                else:
                    return bet_money
            except ValueError:
                print('Введите корректное число.')

    def input_slot(self):
        global list_slot
        while True:
            try:
                bet_slot = int(input('Введите номер слота от 1 до 30: '))
                if 1 <= bet_slot <= 30:
                    return bet_slot
                else:
                    print('ERROR>> Введите номер слота от 1 до 30!')
            except ValueError:
                print('ERROR>> Введите корректное число.')

    def play_game(self):
        global my_money
        global game_over
        global list_slot
        while my_money > 0 and game_over:
            bet_money = self.input_money()
            bet_slot = self.input_slot()

            if bet_slot == list_slot:
                print('Вы выиграли!')
                win_money = bet_money * 2
                print(f'Ваш выигрыш: {win_money}$')
                my_money -= bet_money
                my_money += win_money

            else:
                print('Вы проиграли!')
                print(list_slot)
                my_money -= bet_money


            if my_money != 0 :

                while True:
                    continue_game = input(f'Ваш баланс: {my_money}$.\nХотите продолжить игру? ("да" или "нет"): ').lower()

                    if continue_game == 'нет':
                        print(f'Ваш баланс {my_money}$')
                        print('Игра окончена!')
                        game_over = False
                        break
                    elif continue_game == 'да':
                        break
                    else:
                        print('Введите "да" или "нет"!')


            else:
                print(f'Ваш баланс {my_money}$')
                print('ВЫ ПРОИГРАЛИ ВСЕ ДЕНГИ !\nGAME OVER')


# game = Game()
# game.play_game()