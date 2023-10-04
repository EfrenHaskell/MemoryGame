from tkinter import *
import random
import Home as bd

home = False
retry = False


class Game:
    def __init__(self, title, size, t, item):
        self.game = Tk()
        self.game.title(title)
        self.game.geometry(size)
        self.t = t
        self.item = item
        self.num = 0
        self.game_ar = []
        
    def screen1(self):
        if 'purple' in self.item:
            colors = ['white','white','white','white','white','white','black','black','black','white']
        else:
            colors = ['white','white','white','white','white','white','black','black','black','purple']
        for i in range(self.t):
            col = []
            for j in range(self.t):
                color = colors[random.randint(0, 9)]
                Button(self.game, bg=color, width='4', height='2').grid(row=j, column=i)
                col.append(color)
            self.game_ar.append(col)
        if 'Increased' in self.item:
            self.game.after(46000, self.game.destroy)
            self.game.mainloop()
        else:
            self.game.after(31000, self.game.destroy)
            self.game.mainloop()

    def stats_get(self):
        return self.game_ar


class GameInp:
    def __init__(self, title, size, t, item, mode, stats):
        self.game = Tk()
        self.game.title(title)
        self.game.geometry(size)
        self.t = t
        self.item = item
        self.num = 0
        self.amt = 0
        self.game_ar = stats
        
    def screen2(self):
        button = []
        # global amt
        for i in range(self.t):
            self.amt += self.game_ar[i].count('black')
        
        def sub(m):
            x,y = m
            if self.game_ar[x][y] == 'black':
                # global amt
                button[x][y].destroy()
                self.amt -= 1
                if self.amt == 0:
                    self.game.destroy()
                    print('Good Job!')
                    with open('Game_Storage.txt', 'r') as f:
                        dat = f.read()
                    val = dat.index('*') + 1
                    stats = dat.index('#') + 1
                    dat0 = dat[0:val]
                    dat1 = dat[stats:len(dat)]
                    with open('Game_Storage.txt', 'w') as f:
                        f.write(dat0 + '\nw#' + dat1)
                
            if self.game_ar[x][y] == 'white':
                # global num
                Label(self.game, fg='red', text='X').grid(row=9, column=self.num)
                if self.num >= 3:
                    self.game.destroy()
                    print('Game Over')
                    with open('Game_Storage.txt', 'r') as f:
                        dat = f.read()
                    val = dat.index('*') + 1
                    stats = dat.index('#') + 1
                    dat0 = dat[0:val]
                    dat1 = dat[stats:len(dat)]
                    with open('Game_Storage.txt', 'w') as f:
                        f.write(dat0 + '\nl#' + dat1)
                self.num += 1
                
            if self.game_ar[x][y] == 'purple':
                self.game.destroy()
                print('Game Over')
                with open('Game_Storage.txt', 'r') as f:
                    dat = f.read()
                    f.close()
                val = dat.index('*') + 1
                stats = dat.index('#') + 1
                dat0 = dat[0:val]
                dat1 = dat[stats:len(dat)]
                with open('Game_Storage.txt','w') as f:
                    f.write(dat0 + '\nl#' + dat1)
            
        for i in range(self.t):
            col = []
            for j in range(self.t):
                b = Button(self.game, bg='white', width='4', height='2', command=lambda m=(i, j): sub(m))
                b.grid(row=j, column=i)
                col.append(b)
            button.append(col)
        self.game.mainloop()


def win_screen(moneys, difficulty):
    hub = Tk()
    hub.title('GAME')
    hub.geometry('750x400')
    Label(hub, text='', font=("Arial", 50)).pack()
    Label(hub, text='CONGRATULATIONS', font=("Comic Sans MS", 25)).pack()
    Label(hub, text='YOU WON', font=("Comic Sans MS", 25)).pack()
    Label(hub, text=('YOU HAVE COMPLETED A LEVEL '+str(difficulty)+' PUZZLE'), font=("Comic Sans MS", 25)).pack()
    Label(hub, text='', font=("Arial", 25)).pack()
    Label(hub, text=('Money gained: $' + moneys)).pack()
    Label(hub, text='', font=("Arial", 25)).pack()

    def home():
        hub.destroy()
        with open('Game_Storage.txt', 'r') as f:
            dat = f.read()
        b1 = dat.index('*') + 2
        b2 = dat.index('#')
        dat = dat[b1:b2]
        if dat == 'w':
            with open('Game_Storage.txt', 'r') as f:
                cont = f.read()
                f.close()
            val = cont.index('*')
            mem_num = int(cont[0:val])
            mem_num += 1
            mem_hist = str(mem_num) + '*'
            with open('Game_Storage.txt', 'r') as f:
                dat = f.read()
            num = dat.index('*') + 1
            dat = dat[num:len(dat)]
            with open('Game_Storage.txt', 'w') as f:
                f.write(mem_hist + dat)
            new_h = bd.Hub()
            item = 'n/a'
            new_h.hub_c(item)

    Button(hub, text='Return to Home->', command=home).pack()
    hub.mainloop()


def lose_screen(mode):
    hub = Tk()
    hub.title('GAME')
    hub.geometry('400x400')
    Label(hub, text='', font=("Arial", 50)).pack()
    Label(hub, text='YOU LOST', font=("Comic Sans MS", 25)).pack()
    Label(hub, text='Money gained: $0').pack()
    Label(hub, text='', font=("Arial", 25)).pack()

    def home():
        hub.destroy()
        with open('Game_Storage.txt', 'r') as f:
            dat = f.read()
        star = dat.index('*')
        mem_num = dat[0:star]
        mem_num = int(mem_num)
        if mem_num == 0:
            new_b = bd.Hub()
            new_b.create()
        else:
            new_h = bd.Hub()
            item = 'n/a'
            new_h.hub_c(item)
    Button(hub, text='Return to Home->', command=home).pack()
    hub.mainloop()
    
