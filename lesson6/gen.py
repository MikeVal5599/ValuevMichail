from symbols import colors



def contr(n):
    i = 1 
    derect=False
    while True:
        yield i
        if 1 < i < 5:
            if derect:
                i += 1
            else:
                i -= 1
        else:
            derect = not derect
            if i == 1:
                i += 1
            else:
                i -= 1
def coloris(n):
    colors_numb = len(colors)   
    while True:
        for i in range(colors_numb):
            for _ in range(n):
                yield colors[i]