def time_conversion(string_to_be_converted):
    convert = str(string_to_be_converted)
    if convert.endswith("PM"):
        hour_number = int(convert.split(":")[0])
        minute_number = convert.split(":")[1]
        second_number = convert.split(":")[2].split("PM")[0]
        if hour_number != 12:
            hour_number += 12
        test = hour_number % 24

        if test < 10:
            print("0{}:{}:{}".format(test, minute_number, second_number))
        else:
            print("{}:{}:{}".format(test, minute_number, second_number))

    if convert.endswith("AM"):
        hour_number = int(convert.split(":")[0])
        minute_number = convert.split(":")[1]
        second_number = convert.split(":")[2].split("AM")[0]

        hour_number -= 12
        test = hour_number % 12

        if test < 10:
            print("0{}:{}:{}".format(test, minute_number, second_number))
        else:
            print("{}:{}:{}".format(test, minute_number, second_number))


if __name__ == '__main__':
    # for num in range(0, 24, 1):
    #     if num < 10:
    #         print num
    #         time_conversion("0" + str(num) + ":00:00PM")
    #         time_conversion("0" + str(num) + ":00:00AM")
    #         print "next"
    #     else:
    #         print num
    #         time_conversion(str(num) + ":00:00PM")
    #         time_conversion(str(num) + ":00:00AM")
    #         print "next"
    time_conversion("12:45:54PM")
