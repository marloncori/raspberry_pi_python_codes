
def change_list(data = []):
    for i in range(len(data)+1):
        if(i+1 < 8):
            if(data[i] == 0 and data[i+1] != 0):
                tmp = data[i+1]
                data[i+1] = 0
                data[i] = tmp
        else:
            break
    return data

sample_list = [4, 0, 5, 0, 3, 0, 0, 5]
sample_list.sort(key=change_list, reverse=False)
