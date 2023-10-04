import Home as bd

if __name__ == '__main__':
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
