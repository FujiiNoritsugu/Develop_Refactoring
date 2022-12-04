def sum_before():

    return 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10


def sum_after():
    result = 0
    for i in range(1, 11):
        result += i

    return result


if __name__ == '__main__':
    print(sum_after())
