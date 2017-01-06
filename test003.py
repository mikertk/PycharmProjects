# coding=utf-8
import random


def shout_out(name):
    if name == "虫子":
        print(0)
    elif name == "鸡":
        print(1)
    elif name == "老虎":
        print(2)
    else:
        print(-1)

shout_out(random.choice(["虫子", "鸡", "老虎", "s"]))
print random.choice(["虫子", "鸡", "老虎", "s"])


