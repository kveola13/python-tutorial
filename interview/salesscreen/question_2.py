def efficientJanitor(numbers_to_carry):
    max_weight = 3.00
    sum_weight = 0
    trips = 0
    for numbers in numbers_to_carry:
        end_weight = sum_weight + numbers
        if end_weight >= max_weight:
            trips += 1
            sum_weight = 0
        else:
            sum_weight += numbers
    if sum_weight > 0:
        trips += 1
    return trips


if __name__ == '__main__':
    numbers_array = [
                     1.50,
                     1.50,
                     1.50,
                     1.50,
                     1.50,
                     2.50,
                     0.50
                     ]
    print(efficientJanitor(numbers_array))
