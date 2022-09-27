import os


def print_time(tme: list, clr):
    for row in range(0,5):
        print(clr + tme[0][row]+tme[1][row]+" "+tme[2][row]+tme[3][row]+
        " "+tme[4][row]+tme[5][row]+" "+tme[6][row]+tme[7][row])
def screen_cleaner():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('claer')