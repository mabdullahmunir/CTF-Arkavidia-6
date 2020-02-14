from hashlib import md5
from os import urandom
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

def pack(dec):
    return ("".join((str(key) + ":" + str(dec[key]) + "|") for key in dec)[:-1])

def unpack(enc):
    dec = {}
    enc = enc.split("|")
    for item in enc:
        try:
            dec[item.split(":")[0]] = item.split(":")[1]
        except:
            pass
    return (dec)

def init():
    global key, content, form
    key = urandom(16).encode("hex")
    with open("content.txt", "r") as f:
        content = f.read().splitlines()[0]
        assert 40 <= len(content) <= 50
    form = pack({
        "key": key,
        "content": content,
        "user": "arkav"
    })

def main():
    global key, content, form
    init()
    print("""Welcome 007
[h] Retrieve agent code
[c] Input command
[e] Exit""")
    try:
        while True:
            print("""Select menu:""")
            op = raw_input()
            if op == "h":
                print(md5(form).hexdigest())
            elif op == "c":
                print("""Your command:""")
                msg, sgn = raw_input().split("&")
                msg = form + msg
                if md5(msg).hexdigest() == sgn:
                    msg = unpack(msg)
                    if msg["user"] == "admin" and msg["command"] == "get_flag":
                        print(msg)
                    else:
                        print("You are not 007, go away...")
                else:
                    print("You are not 007, go away...")
            else:
                print("Farewell...")
                exit(0)
    except Exception:
        print("Error detected...")
        exit(0)

if __name__ == '__main__':
    main()
