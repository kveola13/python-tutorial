def shortestSubstring(substring_to_measure):
    string_set = set()
    return_array = []
    for sub_string in substring_to_measure:
        if sub_string not in string_set:
            string_set.add(sub_string)

    if len(string_set) >= 0:
        for iteration in range(len(substring_to_measure)):
            if substring_to_measure[iteration] in string_set:
                string_set.remove(substring_to_measure[iteration])
            return_array.append(substring_to_measure[iteration])
    return len(return_array)


if __name__ == '__main__':
    substring = 'aabcce'
    print(shortestSubstring(substring))
