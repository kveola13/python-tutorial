def jumping_on_clouds(cloud_array):
    next_jump = 0
    jump_count = 0
    for index in range(len(cloud_array) - 3):
        while next_jump + 2 <= len(cloud_array):
            if cloud_array[next_jump + 1] == 0 and cloud_array[next_jump + 2] == 0:
                print("I'm at cloud array: " + str(next_jump))
                print("I will jump to: " + str(next_jump + 2))
                jump_count += 1
                next_jump += 2
            elif cloud_array[next_jump + 1] == 0 and cloud_array[next_jump + 2] == 1:
                print("I'm at cloud array: " + str(next_jump))
                print("I will jump to: " + str(next_jump + 1))
                jump_count += 1
                next_jump += 1
            elif cloud_array[next_jump + 1] == 0:
                print("I'm at cloud array: " + str(cloud_array[next_jump]))
                print("I will jump to: " + str(next_jump + 1))
                jump_count += 1
                next_jump += 1
            elif cloud_array[next_jump + 1] == 1:
                print("I'm at cloud array: " + str(next_jump))
                print("I will jump to: " + str(next_jump + 2))
                jump_count += 1
                next_jump += 2
    return jump_count


def new_jumping_on_clouds(cloud_array):
    jumps = 0
    index = 0
    while index < len(cloud_array) - 1:
        if index + 2 == len(cloud_array) or cloud_array[index + 2] == 1:
            index += 1
            jumps += 1
        else:
            index += 2
            jumps += 1
    return jumps


if __name__ == '__main__':
    clouds = [0, 0, 0, 1, 0, 0]
    print(new_jumping_on_clouds(clouds))
