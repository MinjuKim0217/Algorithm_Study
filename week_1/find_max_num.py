input = [3, 5, 6, 9, 2, 4]


def find_max_num(array):
    max=0
    for i in array:
        if(i>max):
            max=i

    return max


result = find_max_num(input)
print(result)