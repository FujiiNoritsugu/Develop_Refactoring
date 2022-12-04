def print_str(param_str, column_count, row_count):
    len_str = len(param_str)

    if not (5 <= len_str <= 10):
        raise ('文字列は5文字以上10文字以下にしてください')

    if not (param_str.isalpha() and param_str.isascii()):
        raise ('文字列はa～z, A～Zにしてください。')

    for _ in column_count:
        result += param_str
    for _ in row_count:
        print(result)


if __name__ == '__main__':
    print_str('abcef', 3, 5)
