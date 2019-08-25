def odd_numbers(left_number, right_number):
    temp = left_number
    odd_array = []
    while temp <= right_number:
        if temp % 2 == 1:
            odd_array.append(temp)
        temp += 1
    return odd_array


if __name__ == '__main__':
    left = 1
    right = 5
    odd_numbers(left, right)
