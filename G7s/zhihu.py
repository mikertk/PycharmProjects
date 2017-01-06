#!/usr/bin/python
# coding=utf-8

import random

secret = random.randint(1, 100)
print secret
guess = 0
tries = 0
print "AHOY! I'm the Dread Pirate Roberts , and I have a secret!"
print "It is a number from 1 to 99. I'll give you 6 tries . "
while guess != secret and tries < 6:
    try:
        guess = raw_input("What's yer guess? not str! >>>")
        if str(guess).isdigit() != 1:
            print "输入不正确，请输入数字："
        else:
            if int(guess) < secret:
                print "Too low, ye scurvy dog!"
            elif int(guess) > secret:
                print "Too high, landlubber!"
    except:
        if guess < secret:
            print "Too low, ye scurvy dog!"
        elif guess > secret:
            print "Too high, landlubber!"
    tries += 1


if guess == secret:
    print "Avast! Ye got it! Found my secret , ye did!"
else:
    print "No more guesses! Better luck next time , matey!"
    print "The secret number was", secret

print "This is game!"
