from sys import argv
from datetime import datetime


def main(tasks):
    # 今日の曜日を取得（0: 月曜日, 1: 火曜日, ..., 6: 日曜日）
    weekday = datetime.now().weekday()

    # 曜日リスト
    days_of_week = [
        "月曜日",
        "火曜日",
        "水曜日",
        "木曜日",
        "金曜日",
        "土曜日",
        "日曜日",
    ]

    # 曜日順にタスクを出力
    for i in range(7):
        # 今日の曜日を基準に順番を調整
        current_day_index = (weekday + i) % 7
        print(f"{days_of_week[current_day_index]}: {tasks[i]}")


if __name__ == "__main__":
    # 引数の数が7つでなければ、エラーメッセージを表示
    if len(argv) != 8:
        print("曜日ごとのタスクを7つ入力してください。")
        exit(0)

    # コマンドライン引数（最初の引数はスクリプト名なので、argv[1:]でタスクを取得）
    tasks = argv[1:]
    main(tasks)
