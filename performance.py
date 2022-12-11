from random import randint


def print_random1():
    """0～1億の範囲のランダムな数の100万個のリストから0～1億個の範囲のランダムな数の100個のリストが含まれていれば表示する
    """
    base_list = [randint(0, 100000000) for i in range(1000000)]
    checked_list = [randint(0, 100000000) for i in range(100)]
    for temp in checked_list:
        if temp in base_list:
            print(f'temp:{temp} in a')


def print_random2():
    """0～1億の範囲のランダムな数の100万個のセットから0～1億個の範囲のランダムな数の100個のリストが含まれていれば表示する
    """
    base_list = {randint(0, 100000000) for i in range(1000000)}
    checked_list = [randint(0, 100000000) for i in range(100)]
    for temp in checked_list:
        if temp in base_list:
            print(f'temp:{temp} in b')


if __name__ == '__main__':
    print_random1()
