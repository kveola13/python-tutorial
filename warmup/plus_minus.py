def plus_minus(input_numbers):
    positive_counter = 0
    negative_counter = 0
    zero_counter = 0
    for num in range(0, len(input_numbers), 1):
        if input_numbers[num] > 0:
            positive_counter += 1
        if input_numbers[num] == 0:
            zero_counter += 1
        if input_numbers[num] < 0:
            negative_counter += 1
    print("{:.6f}".format(float(positive_counter) / len(input_numbers)))
    print("{:.6f}".format(float(negative_counter) / len(input_numbers)))
    print("{:.6f}".format(float(zero_counter) / len(input_numbers)))


if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())
    plus_minus(arr)
