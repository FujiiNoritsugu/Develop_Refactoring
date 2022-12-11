import numpy as np

MIN_LEN_STR = 5
MAX_LEN_STR = 10


def print_string(param_str, column_count, row_count):
    """文字列を行と列に繰り返し出力する

    Args:
        param_str (str): 表示する文字列
        column_count (int): 列方向に文字列表示を繰り返す数
        row_count (int): 行方向に文字列表示を繰り返す数
    """
    len_str = len(param_str)

    if not (MIN_LEN_STR <= len_str <= MAX_LEN_STR):
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
