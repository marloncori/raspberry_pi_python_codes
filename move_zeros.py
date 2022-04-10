from time import sleep

sample_list = [4, 0, 5, 0, 3, 0, 0, 5]

def zeros_to_the_right(input_data):
    list_length = len(input_data)
    input_data[:] = filter(None, input_data)
    input_data.extend([0] * (list_length - len(input_data)))
    return input_data

def show_list(data, new=False):
    print("=" * 25)
    sleep(0.5)
    if(bool(new)):
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

if __name_ == '__main__':
    try:
        show_list(sample_list)
        zeros_to_the_right(sample_list)
        show_list(sample_list, True)
        
    except (KeyboardInterrupt, SystemExit):
        print(">>>> User has stopped program excution. Goodbye!")
