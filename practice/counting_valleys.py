def counting_valleys(number_of_steps, input_path):
    string_of_paths = input_path
    char_array = []
    steps_up_and_down = 0
    valley_count = 0
    going_down = False
    for char in string_of_paths:
        char_array.append(char)
    for chars in char_array:
        if steps_up_and_down == 0 and chars.upper().lower() == "d":
            going_down = True
        if chars.upper().lower() == "u":
            steps_up_and_down += 1
            print("going up! " + str(steps_up_and_down))
        if chars.upper().lower() == "d":
            steps_up_and_down -= 1
            print("going down! " + str(steps_up_and_down))
        if going_down:
            print("Going down from 0 " + str(going_down))
            valley_count += 1
            going_down = False
    return valley_count


def new_counting_valleys(steps, input):
    steps_up_and_down = 0
    valleys = 0
    for char in input:
        if char == "D":
            steps_up_and_down -= 1
        if char == "U":
            if steps_up_and_down == -1:
                valleys += 1
            steps_up_and_down += 1
    return valleys


if __name__ == '__main__':
    steps = 12
    path = "DDUUDDUDUUUD"
    print(counting_valleys(steps, path))
    print(new_counting_valleys(steps, path))
exit()
