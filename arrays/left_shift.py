def rotate_left(array_of_numbers, given_rotations):
    length = len(array_of_numbers) - 1
    first_num = 0
    for rotation in range(0, given_rotations, 1):
        temp = array_of_numbers[first_num]
        for number in range(length):
            array_of_numbers[number] = array_of_numbers[number + 1]
        array_of_numbers[length] = temp
    return array_of_numbers


def new_rotate_left(array_of_numbers, given_rotations):
    given_rotations %= len(array_of_numbers)
    left_shift = array_of_numbers[given_rotations:] + array_of_numbers[:given_rotations]
    return left_shift


if __name__ == '__main__':
    number_followed_by_rotation = input().split()

    amount_of_numbers = int(number_followed_by_rotation[0])

    rotations = int(number_followed_by_rotation[1])

    array_numbers = list(map(int, input().rstrip().split()))

    print(new_rotate_left(array_numbers, rotations))
