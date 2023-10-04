import time


def timer30(item):
    if 'Increased' in item:
        for i in range(46):
            print(45 - i)
            time.sleep(1)
    else:
        for i in range(31):
            print(30 - i)
            time.sleep(1)
