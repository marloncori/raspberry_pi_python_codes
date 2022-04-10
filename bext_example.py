import bext, random

w, h = bext.size()

def bext_run():
    while True:
        bext.fg('random')
        bext.bg('random')
        x = random.randint(0, w - 1)
        y = random.randint(0, h - 1)
        
        if x == w - 1 and y == h - 1:
            continue # Windows has a weird behavior
        #where a character at the end of the row always moves the cursor to the next row
        bext.goto(x, y)
        print('*', end='')


if __name__ == '__main__':
    try:
        bext_run()
    except (KeyboardInterrupt, SystemExit):
        print(" User has stopped the program. Goodbye!")