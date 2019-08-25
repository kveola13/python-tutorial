def repeated_string(string_to_repeat, occurrences):
    count_in_s = string_to_repeat.count('a')
    print(occurrences // len(
        string_to_repeat * count_in_s + string_to_repeat[0:occurrences % len(string_to_repeat)].count('a')))


if __name__ == '__main__':
    s = input().strip()
    n = int(input().strip())

    count_in_s = s.count('a')
    print(n // len(s) * count_in_s + s[0:n % len(s)].count('a'))