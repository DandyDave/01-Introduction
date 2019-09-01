#!/usr/bin/env python3

import sys
import time
import utils

utils.check_version((3,7))
utils.clear()

print('Hello, Class!')

print('My names Nathaniel Myer')

print('This is hard because it is constantly changing but at the moment my favourite game is Dicey Dungeons, a turn based roughlike which relies on dice rolls.')

print('I am concerned that since im taking 19 credits hours I will not be able to dedicate the time I want to in this class.')

print('I am excited to get some more knowledge about Python since I enjoyed the language the little bit I used it in the class. I am also excited about what it will allow me create.')

print('My stack overflow number is 11980670')

print('My github is https://github.com/DandyDave')

print("~~~~~~~~~~~~~~~~~~~~")
print("| Hey, How Are You |")
print("~~~~~~~~~~~~~~~~~~~~")

time.sleep(3)

choice = input("This is a little text aventure game do you want to play it? [y/n] ")

time.sleep(2)

if choice in ['YES','yes','Yes','y','Y']:
    print("Well... I got this far and got a bit lazy so... this is it. I mean... i guess you win? Yeah?")
else:
    print("Wow!!! I tried so hard and you won't even give it a try. That figures.")
    sys.exit()