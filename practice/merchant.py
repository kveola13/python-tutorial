def sock_merchant(number_of_socks, input_socks):
    pairs = set()
    pair_counter = 0
    for socks in input_socks:
        if socks not in pairs:
            pairs.add(socks)
        elif socks in pairs:
            pair_counter += 1
            pairs.remove(socks)
    return pair_counter


if __name__ == '__main__':
    size = 6
    test_array = [1, 2, 1, 3, 3, 3]
    print(sock_merchant(size, test_array))
