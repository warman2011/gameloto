import random
import copy
import sys

class Game:
    def __init__(self):
        self.listnumbers = [i for i in range(1, 91)]
        self.numb1 = copy.deepcopy(self.listnumbers)
        self.numb2 = copy.deepcopy(self.listnumbers)
        self.numb3 = copy.deepcopy(self.listnumbers)

    def generate_field(self):
        '''   Generate    fields    size 3x9   '''
        self.myfield = [["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]]
        self.computerfield = [["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                              ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                              ["  ", "  ", "     ", "  ", "  ", "  ", "  ", "  ", "  "]]
        i = 0
        ii = 15
        while i < ii:
            i += 1
            num = random.choice(self.numb1)
            self.numb1.remove(num)
            if num == 90:
                self.myfield[2][8] = num
            elif self.myfield[(num % 10) // 4][num // 10] == "  ":
                self.myfield[(num % 10) // 4][num // 10] = num
            else:
                ii += 1
        i = 0
        ii = 15
        while i < ii:
            i += 1
            num = random.choice(self.numb2)
            self.numb2.remove(num)
            if num == 90:
                self.computerfield[2][8] = num
            elif self.computerfield[(num % 10) // 4][num // 10] == "  ":
                self.computerfield[(num % 10) // 4][num // 10] = num
            else:
                ii += 1

    def __str__(self):
        print('ЛОТО'.center(35))
        print('-' * 35 + '\n' + "Билет игрока:".center(35).upper())
        c = list(self.myfield[0]) + list('\n') + list(self.myfield[1]) + list('\n') + list(self.myfield[2])
        print(*c)
        print('-' * 35 + '\n' + "Билет компьютера:".center(35).upper())
        d = list(self.computerfield[0]) + list('\n') + list(self.computerfield[1]) + list('\n') + list(self.computerfield[2])
        print(*d)
        print('-' * 35)
        print(f'Ход номер {90 - len(self.numb3) }, осталось ходов {len(self.numb3)}!')


    # def change_field(self):
    #     """Return random number from """
    #     numb3 = copy.deepcopy(self.listnumbers)
    #     print(numb3)


    def generate_num(self):
        '''Return number from massive'''
        self.num = random.choice(self.numb3)
        self.numb3.remove(self.num)
        return self.numb3

    def next_my(self):
        '''Check number in player field, if field is include number - change to X'''
        for i in range(len(self.myfield)):
            # print(i)
            for j in range(len(self.myfield[i])):
                # print(j)
                if self.myfield[i][j] == self.num:
                    self.myfield[i][j] = " X"
                    # print(self.myfield[i][j])

    def check(self):
        ''' Check player's input command '''
        look = 0
        i = 0
        for i in range(len(self.myfield)):
            look += self.myfield[i].count(self.num)
        self.yn = input(f'Выпало число {self.num}, у Вас есть в билете это число? y/n: ')
        while i != 1:
            if self.yn == 'y' or self.yn == 'n' or self.yn == 'q' :
                i = 1
            else:
                self.yn = input('Вы ввели неверную команду, повторите!')

        if self.yn == 'y' and look == 0:
            print("Вы проиграли!!!!")
            sys.exit()
        if self.yn == 'n' and look != 0:
            print("Вы проиграли!!!!")
            sys.exit()
        if self.yn == 'q':
            sys.exit()


    def next_computer(self):
        '''Check number in computer field, if field is include number - change to X'''
        for i in range(len(self.computerfield)):
            # print(i)
            for j in range(len(self.computerfield[i])):
                # print(j)
                if self.computerfield[i][j] == self.num:
                    self.computerfield[i][j] = "X"
                    # print(self.myfield[i][j])


    def win_or_lose(self):
        '''Check who win and who lose'''
        my_f = 0
        comp = 0
        for i in range(len(self.myfield)):
            for j in range(len(self.myfield[i])):
                if str(self.myfield[i][j]).isdigit():
                    my_f += self.myfield[i][j]
                # print(my_f)
                if str(self.computerfield[i][j]).isdigit():
                    comp += self.computerfield[i][j]
                # print(comp)

        if my_f == 0 and comp == 0:
            print("Победила дружба!!!")
            sys.exit()

        if my_f == 0:
            print("Поздравляю, Вы выиграли!!!")
            sys.exit()

        if comp == 0:
            print("Выиграл компьютер!!!")
            sys.exit()


a = Game()
# print(a.listnumbers)
a.generate_field()
# a.__str__()

while 1 <= len(a.generate_num()):
    a.__str__()
    a.check()
    a.next_my()
    a.next_computer()
    a.win_or_lose()

# print(a.change_field())
# a.generate_num()
# print(a.myfield)
# print(len(a.myfield))
# a.next()

