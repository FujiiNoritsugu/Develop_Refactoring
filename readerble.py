import numpy as np


def print_string(param_str, column_count, row_count):
    len_str = len(param_str)

    if not (5 <= len_str <= 10):
        raise ('文字列は5文字以上10文字以下にしてください')

    if not (param_str.isalpha() and param_str.isascii()):
        raise ('文字列はa～z, A～Zにしてください。')

    result_str = ''
    for _ in range(column_count):
        result_str += param_str
    for _ in range(row_count):
        print(result_str)


if __name__ == '__main__':
    print_string(
        'abcef', np.random.randint(
            0, 10), np.random.randint(
            0, 10))
