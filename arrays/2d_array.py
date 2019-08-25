def hourglass_sum(input_array):
    global temp, biggest_number
    biggest_number = -20
    for index in range(0, 4, 1):
        for second_index in range(0, 4, 1):
            temp = input_array[index][second_index] + input_array[index][second_index + 1] + \
                   input_array[index][second_index + 2] + input_array[index + 1][second_index + 1] + \
                   input_array[index + 2][second_index] + input_array[index + 2][second_index + 1] + \
                   input_array[index + 2][second_index + 2]
            biggest_number = max(temp, biggest_number)
    return biggest_number


if __name__ == '__main__':

    array = []

    for _ in range(6):
        array.append(list(map(int, input().rstrip().split())))

    print(hourglass_sum(array))
