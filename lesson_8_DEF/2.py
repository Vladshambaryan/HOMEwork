import random
import os
import sys
from utils import helper
from utils.helper import assist as assist1
from random import random, randint, randrange, choice
from utils.help2 import assist as assist2
from utils.help2 import very_useful_function_for_your_easy_life as userful


print(os.O_RANDOM)
print(sys.platform)

print(random())
print(f'Your prise is {int(random() * 100)}')
print(randint(0, 5))
print(randrange(0, 20, 2))

user = ['user11', 'user12', 'user100']
print(choice(user))
print(user[randrange(0, len(user))])

assist1()
helper.assist()
print(helper.variable)

assist2()

while 'sldkjfl' == 'sdsdfsdf':
    if 'sldkjfl' == 'sdsdfsdf':
        print(f'skadflkasdjfhalsdkjhlaksdfjhlaksjdfh {userful()}')