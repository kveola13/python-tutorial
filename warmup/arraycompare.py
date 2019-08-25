def compare_triplets(first, second):
    if len(first) == len(second):
        result_list = [0, 0]
        for num in range(0, len(first), 1):
            if first[num] > second[num]:
                result_list[0] += 1
                print("incremented first" + str(result_list))
            elif first[num] < second[num]:
                result_list[1] += 1
                print("incremented second" + str(result_list))
        return result_list


if __name__ == '__main__':
    first_list = [1, 2, 3]
    second_list = [3, 2, 1]
    compare_triplets(first_list, second_list)
