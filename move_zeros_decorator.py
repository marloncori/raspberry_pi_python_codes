from time import sleep
from list_decorator import show_list

sample_list = [4, 0, 5, 0, 3, 0, 0, 5]

@show_list
def zeros_to_the_right(input_data, new=False):
    list_length = len(input_data)
    input_data[:] = filter(None, input_data)
    input_data.extend([0] * (list_length - len(input_data)))
    return input_data


if __name__ == '__main__':
    try:
        zeros_to_the_right(sample_list, True)
        
    except (KeyboardInterrupt, SystemExit):
        print(">>>> User has stopped program excution. Goodbye!")

