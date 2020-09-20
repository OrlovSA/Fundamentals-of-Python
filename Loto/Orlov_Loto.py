import random


class Kegs:
    def __init__(self):
        self.kegs = self._num()
        self.kegs_user = self.kegs[:15]
        self.kegs_comp = self.kegs[15:30]
        random.shuffle(self.kegs)

    def _num(self):
        kegs = [i for i in range(1, 91)]
        random.shuffle(kegs)
        return kegs


class Loto():
    def __init__(self, kegs, name, num_in, num_out):
        self.kegs = kegs
        self.name = name
        self.num_in = num_in
        self.num_out = num_out
        self.card_nums = self.kegs
        self.card_nums.sort()
        self._card = self._card_generation()

    def _card_generation(self):
        card = ''
        for _ in range(3):
            x = [' {}'] * 5 + ([' '] * 4)
            random.shuffle(x)
            x += ['\n']
            card += ' '.join(x)
        return card

    @property
    def card(self):
        result = self._card.format(*self.card_nums)
        return f'{self.name}{result}---------Баллы: {self.card_nums.count("--")}/15 ---------'


def input_check():
    x = ['y', 'n']
    while True:
        try:
            i = str(input('Зачеркнуть цифру? (y/n)\n')).lower()
            if i not in x:
                print('неверный ввод.')
            else:
                return i
        except:
            print('введите букву.')


class Game:
    def __init__(self, user, comp, nums):
        self.user = user
        self.comp = comp
        self.nums = nums

    @property
    def game_start(self):
        for i, num in enumerate(nums.kegs, 1):
            print(f'Новый бочонок: {num} (осталось {90-i})')
            print(comp.card)
            print(user.card)

            if num in comp.card_nums:
                comp.card_nums.insert(comp.card_nums.index(num), '--')
                comp.card_nums.remove(num)
            if comp.card_nums.count('--') == 15:
                print('Карточка компьютера Победила!\nВы проиграли!')
                break

            input_user = input_check()
            if input_user =='y':
                if num in user.card_nums:
                    user.card_nums.insert(user.card_nums.index(num), '--')
                    user.card_nums.remove(num)
                    print('Верно')
                else:
                    print(f'Цифрв в вашей карте отсутствует!\n{user.card}\nВы проиграли!')
                    break
            if input_user == 'n':
                if num in user.card_nums:
                    print(f'Цифра в вашей карте была!\n{user.card}\nВы проиграли!')
                    break
            if user.card_nums.count('--') == 15:
                print('Ваша Карточка Победила!')
                break
        return 'Игра закончина!'


nums = Kegs()
comp = Loto(nums.kegs_comp, '-- Карточка компьютера ---\n', 0, 15)
user = Loto(nums.kegs_user, '------ Ваша карточка -----\n', 15, 30)
game = Game(user, comp, nums)
game.game_start