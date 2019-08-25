def find_number(input_array, input_number):
    if input_number in input_array:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    array = [3, 2, 3, 1, 5]
    number = 6
    find_number(array, number)
