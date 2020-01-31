# a = map(int, input().split())

from random import randint

state01 = 1
state02 = 2
state03 = 4
state04 = 5

win_coef01 = int(100 + randint(1, 30 + state01 * 60)) // 100
win_coef02 = int(100 + randint(1, 30 + state02 * 60)) // 100
win_coef03 = int(100 + randint(1, 30 + state03 * 60)) // 100
win_coef04 = int(100 + randint(1, 30 + state04 * 60)) // 100

print(f'''{win_coef01}
{win_coef02}
{win_coef03}
{win_coef04}''')