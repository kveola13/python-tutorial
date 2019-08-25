def mini_max(input_numbers):
    mini_number = min(input_numbers)
    maxi_number = max(input_numbers)
    mini_sum = long(0)
    maxi_sum = long(0)
    for num in range(0, len(input_numbers), 1):
        if input_numbers[num] == maxi_number:
            continue
        mini_sum += input_numbers[num]
    for num in range(0, len(input_numbers), 1):
        if input_numbers[num] == mini_number:
            continue
        maxi_sum += input_numbers[num]
    print("{} {}".format(long(mini_sum), long(maxi_sum)))


def new_mini_max(input_numbers):
    all_results = []
    for index in range(len(input_numbers)):
        result = sum(input_numbers) - input_numbers[index]
        all_results.append(result)
    print (min(all_results), max(all_results))


if __name__ == '__main__':
    arr = (map(int, raw_input().rstrip().split()))

    mini_max(arr)
