from time import sleep

def show_list(func):
    def inner(*args, **kwargs):
        print("=" * 25)
        data = func(*args, **kwargs)
        sleep(0.5)
        if(bool(**kwargs)):
            print(" New list: [")
            sleep(1)
        else:
            print(" Sample list: [")
            sleep(1)
        for x in data:
            print(x, end=" ")
            sleep(0.5)
        print("].")
        sleep(0.5)
        print("=" * 25)
        
    return inner
