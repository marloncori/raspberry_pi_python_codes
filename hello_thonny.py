from time import sleep

msg = "Hi, Python!"
space = "\t"
colors = ["\033[1;29m", "\033[1;31m", "\033[1;32m", "\033[1;33m",
          "\033[1;34m", "\033[1;35m", "\033[1;36m", "\033[1;37m", "\033[1;30m"]

for c in range(len(colors)):
    print(colors[c] + msg + "\033[0m")
    msg = space + msg
    sleep(1)