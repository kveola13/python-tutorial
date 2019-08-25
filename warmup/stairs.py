def stairs(amount_of_stairs):
    space_counter = amount_of_stairs - 1
    pound_counter = 1
    for number in range(0, amount_of_stairs, 1):
        space_inserter = " " * space_counter
        pound_inserter = "#" * pound_counter
        print space_inserter + pound_inserter
        pound_counter += 1
        space_counter -= 1


if __name__ == '__main__':
    amount_of_steps = int(input())
    stairs(amount_of_steps)
