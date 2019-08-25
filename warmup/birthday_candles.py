def birthday_cake_candles(input_numbers):
    count = 0
    maxi_number = max(input_numbers)
    for index in range(len(input_numbers)):
        if input_numbers[index] == maxi_number:
            count += 1
    print(count)


if __name__ == '__main__':
    ar_count = int(input())

    array_of_numbers = (map(int, raw_input().rstrip().split()))

    birthday_cake_candles(array_of_numbers)
