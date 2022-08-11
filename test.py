from tabnanny import check
import threading
import time

check1 = True
check2 = True
check3 = True

def check_input():
    global check1
    check1 = False
    time.sleep(1)
    print("Check input!")
    check1 = True
    
def update():
    global check2
    check2 = False
    time.sleep(0.5)
    print("update...")
    check2 = True

def others():
    global check3
    check3 = False
    time.sleep(0.05)
    print("others...")
    check3 = True

#while True:
#    if check1: threading.Thread(target=check_input).start()
#    if check2: threading.Thread(target=update).start()
#    if check3: threading.Thread(target=others).start()
    

class test:
    def __init__(self):
        self.list = []

    def func1(self):
        list = self.func2()
        [print(i ** 3) for i in list]

    def func2(self):
        [i ** 3 for i in range(1000000)]

c = test()
start = time.time()
threading.Thread(target=c.func1).start()
threading.Thread(target=c.func2).start()
end = time.time()

print(c.list)
print(end - start)