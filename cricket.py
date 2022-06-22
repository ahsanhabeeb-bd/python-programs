import random


class cricket:

    def __init__(self):
        self.boll = 0
        self.over = 0
        self.wh_no = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'n', 'n', 'w', 'w']
        self.wn = []
        self.ru_nr = [0, 1, 2, 3, 4, 6]
        self.run = 0
        self.total_run = 0
        self.player = ['ak', 'aj', 'ai', 'ah', 'ag', 'af', 'ae', 'ad', 'ac', 'ab', 'aa']
        self.wicket_out = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, ]
        self.out = 0
        self.wicket = 0
        self.total_wicket = 0
        self.player1 = 0
        self.player2 = 0
        self.out_player_list = []
        self.out_player_run_list = []
        self.player_run = []
        self.player_total_run = 0
        self.player_out_run = {}
        self.run_over = []
        self.over_total_run = 0
        self.total_w = 0
        self.total_n = 0
        self.total_ext = 0

    def team_name(self):
        return f'TEAM A'

    def boll_(self):
        self.wn = random.choice(self.wh_no)
        if self.wn == 0:
            self.boll += 1
            return self.boll
        elif self.wn == 'n':
            self.boll = self.boll
            return self.boll
        elif self.wn == 'w':
            self.boll = self.boll
            return self.boll

    def over_(self):
        if self.boll == 6:
            self.over += 1
            self.boll = 0
            return self.over

    def run_over_(self):
        if self.boll == 1 and self.over > 0 and self.wn == 0:
            self.run_over.clear()
            self.over_total_run = 0
            return self.run_over ,self.over_total_run

    def player_(self):
        if self.wicket == 0:
            self.player1 = self.player[-1]
            self.player2 = self.player[-2]
            return self.player1, self.player2
        elif self.wicket == 1:
            self.player1 = self.player[-1]
            self.player.pop()

            self.player1 = self.player2
            self.player2 = self.player[-2]
            return self.player1, self.player2

    def wicket_(self):
        if self.wn == 0:
            self.wicket = random.choice(self.wicket_out)
            if self.wicket == 1:
                self.out_player_run_list.append(self.player_total_run)
                self.out_player_list.append(self.player1)
                self.player_out_run = dict(zip(self.out_player_list, self.out_player_run_list))
                self.out = f'OUT "{self.player1}"'
                return self.out, self.out_player_run_list, self.out_player_list, self.player_out_run
        elif self.wn == 'n':
            self.wicket = 0
            return self.wicket
        elif self.wn == 'w':
            self.wicket = 0
            return self.wicket

    def total_wicket_(self):
        if self.wicket == 1:
            self.total_wicket += self.wicket
            return self.total_wicket

    def run_(self):
        if self.wn == 0 and self.wicket == 1:
            self.run = 0
            self.player_run.clear()
            self.player_total_run = 0
            self.run_over.append('W')
            self.over_total_run = self.over_total_run
            return self.run, self.player_run, self.run_over , self.over_total_run

        elif self.wn == 0 and self.wicket == 0:
            self.run = random.choice(self.ru_nr)
            self.player_run.append(self.run)

            self.run_over.append(str(self.run))
            self.player_total_run = sum(self.player_run)
            self.over_total_run += self.run
            return self.run, self.player_total_run, self.run_over ,self.over_total_run

        elif self.wn == 'n':
            self.run = random.choice(self.ru_nr) + 1
            self.player_run.append(self.run - 1)
            self.player_total_run = sum(self.player_run)
            self.run_over.append(str(self.run)+'N')
            self.over_total_run += self.run
            self.total_n += 1
            return self.run, self.player_total_run, self.run_over ,self.over_total_run ,self.total_n

        elif self.wn == 'w':
            self.run = 1
            self.player_run.append(0)
            self.run_over.append(str(self.run)+'W')
            self.player_total_run = sum(self.player_run)
            self.over_total_run += self.run
            self.total_w += 1
            return self.run, self.player_total_run, self.run_over ,self.total_w

    def total_run_(self):
        self.total_run += self.run
        self.total_ext = self.total_w+self.total_n
        return self.total_run,self.total_ext


c1 = cricket()
print(c1.team_name())

while c1.over != 3 and c1.total_wicket != 10 :

    c1.boll_()
    c1.over_()
    c1.run_over_()
    c1.player_()
    c1.wicket_()
    c1.total_wicket_()
    c1.run_()
    c1.total_run_()

    if c1.wn == 0:
        if c1.wicket == 1:
            print(
                f'{c1.boll}.{c1.over} {c1.out} {c1.run_over} {c1.over_total_run} \n{c1.total_run}/{c1.total_wicket}  {c1.player1}*,{c1.player2},{c1.player_out_run}\n')
        elif c1.wicket == 0:
            print(
                f'{c1.boll}.{c1.over} run = {c1.run} {c1.run_over} {c1.over_total_run} \n{c1.total_run}/{c1.total_wicket}  {c1.player1}*,{c1.player2} {c1.player_run} {c1.player_total_run}\n')

    elif c1.wn == 'n':
        print(
            f'{c1.boll}(N).{c1.over} run = ({c1.run - 1} +1) {c1.run_over} {c1.over_total_run} \n{c1.total_run}/{c1.total_wicket}  {c1.player1}*,{c1.player2} {c1.player_run} {c1.player_total_run}\n')
    elif c1.wn == 'w':
        print(
            f'{c1.boll}(W).{c1.over} run = ({c1.run - 1} +1) {c1.run_over} {c1.over_total_run} \n{c1.total_run}/{c1.total_wicket}  {c1.player1}*,{c1.player2} {c1.player_run} {c1.player_total_run}\n')
print(f'Total Over = {c1.boll}.{c1.over} \nTotal Run = {c1.total_run} \nTotal Wicket = {c1.total_wicket} \nPlayer Run {c1.player_out_run} \nTotal No Ball = {c1.total_n}'
      f'\nTotal White Boll = {c1.total_w}\nTotal Extra = {c1.total_ext}\n\n')



import random


class cricket2:

    def __init__(self):
        self.boll = 0
        self.over = 0
        self.wh_no = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'n', 'n', 'w', 'w']
        self.wn = []
        self.ru_nr = [0, 1, 2, 3, 4, 6]
        self.run = 0
        self.total_run = 0
        self.player = ['ak', 'aj', 'ai', 'ah', 'ag', 'af', 'ae', 'ad', 'ac', 'ab', 'aa']
        self.wicket_out = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, ]
        self.out = 0
        self.wicket = 0
        self.total_wicket = 0
        self.player1 = 0
        self.player2 = 0
        self.out_player_list = []
        self.out_player_run_list = []
        self.player_run = []
        self.player_total_run = 0
        self.player_out_run = {}
        self.run_over = []
        self.over_total_run = 0
        self.total_w = 0
        self.total_n = 0
        self.total_ext = 0

    def team_name(self):
        return f'TEAM B'

    def boll_(self):
        self.wn = random.choice(self.wh_no)
        if self.wn == 0:
            self.boll += 1
            return self.boll
        elif self.wn == 'n':
            self.boll = self.boll
            return self.boll
        elif self.wn == 'w':
            self.boll = self.boll
            return self.boll

    def over_(self):
        if self.boll == 6:
            self.over += 1
            self.boll = 0
            return self.over

    def run_over_(self):
        if self.boll == 1 and self.over > 0 and self.wn == 0:
            self.run_over.clear()
            self.over_total_run = 0
            return self.run_over ,self.over_total_run

    def player_(self):
        if self.wicket == 0:
            self.player1 = self.player[-1]
            self.player2 = self.player[-2]
            return self.player1, self.player2
        elif self.wicket == 1:
            self.player1 = self.player[-1]
            self.player.pop()

            self.player1 = self.player2
            self.player2 = self.player[-2]
            return self.player1, self.player2

    def wicket_(self):
        if self.wn == 0:
            self.wicket = random.choice(self.wicket_out)
            if self.wicket == 1:
                self.out_player_run_list.append(self.player_total_run)
                self.out_player_list.append(self.player1)
                self.player_out_run = dict(zip(self.out_player_list, self.out_player_run_list))
                self.out = f'OUT "{self.player1}"'
                return self.out, self.out_player_run_list, self.out_player_list, self.player_out_run
        elif self.wn == 'n':
            self.wicket = 0
            return self.wicket
        elif self.wn == 'w':
            self.wicket = 0
            return self.wicket

    def total_wicket_(self):
        if self.wicket == 1:
            self.total_wicket += self.wicket
            return self.total_wicket

    def run_(self):
        if self.wn == 0 and self.wicket == 1:
            self.run = 0
            self.player_run.clear()
            self.player_total_run = 0
            self.run_over.append('W')
            self.over_total_run = self.over_total_run
            return self.run, self.player_run, self.run_over , self.over_total_run

        elif self.wn == 0 and self.wicket == 0:
            self.run = random.choice(self.ru_nr)
            self.player_run.append(self.run)
            self.run_over.append(str(self.run))
            self.player_total_run = sum(self.player_run)
            self.over_total_run += self.run
            return self.run, self.player_total_run, self.run_over ,self.over_total_run

        elif self.wn == 'n':
            self.run = random.choice(self.ru_nr) + 1
            self.player_run.append(self.run - 1)
            self.player_total_run = sum(self.player_run)
            self.run_over.append(str(self.run)+'N')
            self.over_total_run += self.run
            self.total_n += 1
            return self.run, self.player_total_run, self.run_over ,self.over_total_run ,self.total_n

        elif self.wn == 'w':
            self.run = 1
            self.player_run.append(0)
            self.run_over.append(str(self.run)+'W')
            self.player_total_run = sum(self.player_run)
            self.over_total_run += self.run
            self.total_w += 1
            return self.run, self.player_total_run, self.run_over ,self.total_w

    def total_run_(self):
        self.total_run += self.run
        self.total_ext = self.total_w+self.total_n
        return self.total_run,self.total_ext


c2 = cricket2()
print(c2.team_name())

while c2.over != 3 and c2.total_wicket != 10 :

    c2.boll_()
    c2.over_()
    c2.run_over_()
    c2.player_()
    c2.wicket_()
    c2.total_wicket_()
    c2.run_()
    c2.total_run_()

    if c2.wn == 0:
        if c2.wicket == 1:
            print(
                f'{c2.boll}.{c2.over} {c2.out} {c2.run_over} {c2.over_total_run} \n{c2.total_run}/{c2.total_wicket}  {c2.player1}*,{c2.player2},{c2.player_out_run}\n')
        elif c2.wicket == 0:
            print(
                f'{c2.boll}.{c2.over} run = {c2.run} {c2.run_over} {c2.over_total_run} \n{c2.total_run}/{c2.total_wicket}  {c2.player1}*,{c2.player2} {c2.player_run} {c2.player_total_run}\n')

    elif c2.wn == 'n':
        print(
            f'{c2.boll}(N).{c2.over} run = ({c2.run - 1} +1) {c2.run_over} {c2.over_total_run} \n{c2.total_run}/{c2.total_wicket}  {c2.player1}*,{c2.player2} {c2.player_run} {c2.player_total_run}\n')
    elif c2.wn == 'w':
        print(
            f'{c2.boll}(W).{c2.over} run = ({c2.run - 1} +1) {c2.run_over} {c2.over_total_run} \n{c2.total_run}/{c2.total_wicket}  {c2.player1}*,{c2.player2} {c2.player_run} {c2.player_total_run}\n')
print(f'Total Over = {c2.boll}.{c2.over} \nTotal Run = {c2.total_run} \nTotal Wicket = {c2.total_wicket} \nPlayer Run {c2.player_out_run} \nTotal No Ball = {c2.total_n}'
      f'\nTotal White Boll = {c2.total_w}\nTotal Extra = {c2.total_ext}\n\n')

