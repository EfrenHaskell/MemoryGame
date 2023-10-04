import threading
import timer as t
import Game as b


class Gamers:
    def __init__(self, title, size, t, item, mode):
        self.title = title
        self.size = size
        self.t = t
        self.item = item
        self.mode = mode
        
    def start_game1(self):
        self.gm = b.Game(self.title, self.size, self.t, self.item)
        self.gm.screen1()

    def start_timer1(self):
        print('Starting Timer:')
        self.timer = t.timer30(self.item)
    
    def run_thread1(self):
        t1 = threading.Thread(target=self.start_game1)
        t2 = threading.Thread(target=self.start_timer1)

        t1.start()
        t2.start()

        t1.join()
        t2.join()
        return self.gm.stats_get()

class g_inp:
    def __init__(self, title, size, t, item, mode, stats):
        self.title = title
        self.size = size
        self.t = t
        self.item = item
        self.mode = mode
        self.stats = stats
    
    def start_game2(self):
        self.gm = b.GameInp(self.title, self.size, self.t, self.item, self.mode, self.stats)
        self.gm.screen2()
        with open('Game_Storage.txt','r') as f:
            dat = f.read()
        b1 = dat.index('*') + 2
        b2 = dat.index('#')
        dat = dat[b1:b2]
        moneys = 0
        if 'Double' in self.item:
            moneys = int(100 * (1.4 ** self.t))
            moneys = str(moneys)
        if 'Triple' in self.item:
            moneys = int(150 * (1.4 ** self.t))
            moneys = str(moneys)
        if self.item == 'n/a':
            moneys = int(50 * (1.4 ** self.t))
            moneys = str(moneys)
        
        if dat == 'w':
            with open('Game_Storage.txt', 'r') as f:
                dat = f.read()
            num = dat.index('#') + 2
            num1 = dat.index('$')
            mons = int(dat[num:num1])
            mons += int(moneys)
            mons = str(mons)
            i1 = dat.index('#') + 1
            dat = dat[0:i1]
            with open('Game_Storage.txt', 'w') as f:
                f.write(dat + '\n' + mons + '$')
            b.win_screen(moneys, self.t)
            
        else:
            b.lose_screen(self.mode)



