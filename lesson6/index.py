import datetime
import time
from unicodedata import name

from symbols import SEPAR, NUMBERS
from gen import contr, coloris
from utils import print_time, screen_cleaner

def main():
    cntr = contr(5)
    clr= coloris(10)
    while True:
        current_numbers=[]
        tme = datetime.datetime.now().strftime("%H%M%S")
        separator=SEPAR[next(cntr)]
        current_numbers.append(NUMBERS[int(tme[0])])
        current_numbers.append(NUMBERS[int(tme[1])])
        current_numbers.append(separator)
        current_numbers.append(NUMBERS[int(tme[2])])
        current_numbers.append(NUMBERS[int(tme[3])])
        current_numbers.append(separator)
        current_numbers.append(NUMBERS[int(tme[4])])
        current_numbers.append(NUMBERS[int(tme[5])])
        color=next(clr)
        print_time(current_numbers, color)
        time.sleep(0.2)
        screen_cleaner()


