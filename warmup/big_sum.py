def a_very_big_sum(range_of_numbers, numbers_to_add):
    the_sum = 0
    for index in range(0, range_of_numbers, 1):
        the_sum += numbers_to_add[index]
    print(the_sum)
    return the_sum


if __name__ == '__main__':
    amount_of_numbers = int(input())

    list_of_numbers = [1000, 1000, 10000, 10000000, 1000]

    a_very_big_sum(amount_of_numbers, list_of_numbers)
