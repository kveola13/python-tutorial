def diagonal_difference(input_numbers):
    counter = 0
    second_counter = len(input_numbers) - 1
    first_array = []
    second_array = []
    for index in range(len(input_numbers)):
        first_array.append(input_numbers[counter][counter])
        counter += 1
    counter = 0
    for index in range(len(input_numbers)):
        second_array.append(input_numbers[counter][second_counter])
        counter += 1
        second_counter -= 1
    print first_array
    print second_array
    return abs(sum(first_array) - sum(second_array))


if __name__ == '__main__':
    size = int(input())

    number_array = []

    for _ in range(size):
        number_array.append(map(int, raw_input().rstrip().split()))
    diagonal_difference(number_array)
