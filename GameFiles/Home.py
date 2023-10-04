from tkinter import *
import game_thread as gt
import random

diff = 8
item_get = 'n/a'


class Hub:
    def __init__(self):
        self.hub = Tk()
        self.hub.title('HOME')
        self.hub.geometry('420x420')

    def create(self):
        Label(self.hub, text='Welcome to the game').pack()
        Label(self.hub, text='Here are the rules: ').pack()
        Label(self.hub, text='1. A screen will temporarily appear').pack()
        Label(self.hub, text='Memorize the pattern before the time runs out').pack()
        Label(self.hub, text='2. The next screen will be entirely white').pack()
        Label(self.hub, text='Replace all the black tiles').pack()
        Label(self.hub, text='3. For white tiles:').pack()
        Label(self.hub, text='You can fuck up and misplace a black tile 4 times before Game Over').pack()
        Label(self.hub, text='4. For purple tiles:').pack()
        Label(self.hub, text='If you place a black tile where a purple tile should be you immediately lose').pack()
        Label(self.hub, text='5. A timer will show up in your shell').pack()
        Label(self.hub, text='You have 30 seconds to memorize, after which you must recreate the pattern').pack()

        def start():
            self.hub.destroy()
            self.hub.mainloop()
            tut = gt.Gamers('TUTORIAL', '230x280',6, 'n/a', 't')
            stats = tut.run_thread1()
            tut1 = gt.g_inp('TUTORIAL', '230x280', 6, 'n/a', 't', stats)
            tut1.start_game2()
                
        Button(self.hub, text='Begin Tutorial', command=start).pack()
        
    def hub_c(self, item):
        with open('Game_Storage.txt', 'r') as f:
            dat = f.read()
        num = dat.index('#') + 2
        num1 = dat.index('$')
        mons = dat[num:num1]

        with open('Game_Storage.txt', 'r') as f:
            stuff = f.read()
        val = stuff.index('*') + 1
        stats = stuff.index('#') + 1
        dat0 = stuff[0:val]
        dat1 = stuff[stats:len(stuff)]
        with open('Game_Storage.txt', 'w') as f:
            f.write(dat0 + '\n_#' + dat1)
        mem_num = 0
        with open('Game_Storage.txt', 'r') as f:
            cont = f.read()
        star = cont.index('*')
        mem_num = cont[0:star]
        mem_num = int(mem_num)
        
        Label(self.hub, text='Welcome!', font=('Comic Sans MS', 15)).pack()
        Label(self.hub, text=('Money: ' + mons)).pack()
        Label(self.hub, text=('Wins: ' + str(mem_num))).pack()
        
        def start():
            self.hub.destroy()
            self.hub.mainloop()
            dim = str(diff * 38) + 'x' + str(diff * 47)
            game = gt.Gamers('GAME', dim, diff, item, 'g')
            stats = game.run_thread1()
            game1 = gt.g_inp('GAME', dim, diff, 'n/a', 'g', stats)
            game1.start_game2()
        Label(self.hub, text='', font=('Arial', 5)).pack()
        Label(self.hub, text='Input a number of tiles below').pack()
        Label(self.hub, text='(no greater than 14, no smaller than 5)').pack()
        Label(self.hub, text='Then click begin game to start').pack()
        if item != 'n/a':
            Label(self.hub, text=('Using: ' + item)).pack()
        
        def sub():
            val = int(e0.get())
            if val <= 4 or val > 14:
                print('Please input a valid number')
            else:
                print('Game mode tiles set to', val)
                global diff
                diff = val
        e0 = Entry(self.hub)
        e0.pack()
        Button(self.hub, width=10, text="Level Input", command=sub).pack()
        Button(self.hub, text='Begin Game', command=start).pack()
        Label(self.hub, text='', font=('Arial', 10)).pack()

        def shop():
            items = ['Double money', 'Triple money', 'No purple', 'Increased time']
            self.hub.destroy()
            self.hub.mainloop()
            self.shop = Tk()
            self.shop.title('SHOP')
            self.shop.geometry('325x350')
            Label(self.shop, text='Welcome to the Shop', font=('Comic Sans MS', 15)).pack()
            Label(self.shop, text='', font=('Arial', 10)).pack()
            Label(self.shop, text='You can only use one item at a time').pack()
            Label(self.shop, text='If you buy multiple items, only the last one will be saved').pack()
            Label(self.shop, text='Items are randomly allocated').pack()
            Label(self.shop, text='An item is immediately applied to the next game').pack()
            Label(self.shop, text='All items will be lost once you close the program').pack()
            Label(self.shop, text='', font=('Arial', 10)).pack()
            Label(self.shop, text='Price: 1500').pack()

            def buy():
                with open('Game_Storage.txt', 'r') as f:
                    dat = f.read()
                num = dat.index('#') + 2
                num1 = dat.index('$')
                mons = int(dat[num:num1])
                if mons < 1500:
                    print('You are broke af, you can\'t buy that')
                else:
                    mons -= 1500
                    mons = str(mons)
                    i1 = dat.index('#') + 1
                    dat = dat[0:i1]
                    with open('Game_Storage.txt', 'w') as f:
                        f.write(dat + '\n' + mons + '$')
                    global item_get
                    item_get = items[random.randint(0, 3)]
                    Label(self.shop, text=('You got: ' + item_get), font=('Arial', 10)).pack()
                    
            Button(self.shop, text='Buy Item', command=buy).pack()
            Label(self.shop, text='', font=('Arial', 15)).pack()

            def hreturn():
                self.shop.destroy()
                self.shop.mainloop()
                new_h = Hub()
                new_h.hub_c(item_get)
            Button(self.shop, text='<-Return to Home', command=hreturn).pack()
        Label(self.hub, text='With money you can buy items in the shop').pack()
        Button(self.hub, text='Open Shop->', command=shop).pack()
        
        
        
    



