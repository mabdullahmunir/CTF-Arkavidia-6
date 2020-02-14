from random import *
from string import *
from Crypto.Util.number import long_to_bytes as lb, bytes_to_long as bl
import sys


class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

def inc():
    global flag, ctr, go, e, n, pt, ct
    ctr += ctr + 1
    return (ctr)

def enc():
    global flag, ctr, go, e, n, pt, ct
    ct = pow(inc() * bl(pt) + (inc() << len(bin(bl(flag + "".join(choice(ascii_uppercase + ascii_lowercase + digits) for _ in range(16))))[2:])), e, n)

def mod():
    global flag, ctr, go, e, n, pt, ct
    with open("modulus.txt", "r") as f:
        n = int(next(f)[:-1])
        for i, n2 in enumerate(f, 2):
            if randrange(i):
                continue
            n = int(n2[:-1])

def init():
    global flag, ctr, go, e, n, pt, ct
    with open("flag.txt", "r") as f:
        flag = f.read()[:54]
    pt = flag + "".join(choice(ascii_uppercase + ascii_lowercase + digits) for _ in range(16))
    ctr = 0; e = 5; go = True
    mod(); enc()

def main():
    global flag, ctr, go, e, n, pt, ct
    init()
    while go:
        print("=======================")
        print("""Welcome to Gacha Universe
Your modulus: {}
Your ciphertext: {}\n""".format(n, ct))
        print("""Menu:
1. Get new ciphertext
2. Get new modulus
3. Restart program
4. Exit
Select menu: """)
        op = raw_input()
        try:
            if op == "1":
                enc()
            elif op == "2":
                mod()
            elif op == "3":
                init()
                print("Restarted...")
            elif op == "4":
                go = False
        except Exception as error:
            print("Error detected...")
            print(error)
        finally:
            print("=======================\n\n")

if __name__ == '__main__':
    main()
