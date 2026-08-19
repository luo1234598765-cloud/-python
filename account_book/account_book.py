import json
from pathlib import Path

data_file = Path(__file__).with_name("records.json")


def load_records():
    try:
        with open(data_file, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_records(records):
    with open(data_file, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)


records = load_records()

print(f"已读取 {len(records)} 笔历史记录。")

while True:
    action = input("请选择操作：添加 / 查看 / 退出：")

    if action == "添加":
        item = input("请输入项目名称：")
        amount = float(input("请输入金额："))
        record_type = input("请输入类型：收入 或 支出：")

        record = {
            "项目": item,
            "金额": amount,
            "类型": record_type,
        }

        records.append(record)
        save_records(records)
        print("已添加并保存一笔记录。")

    elif action == "查看":
        total_income = 0
        total_expense = 0

        print("----- 账目明细 -----")

        for record in records:
            print(f"{record['类型']}｜{record['项目']}｜{record['金额']:.2f} 元")

            if record["类型"] == "收入":
                total_income = total_income + record["金额"]
            elif record["类型"] == "支出":
                total_expense = total_expense + record["金额"]

        balance = total_income - total_expense

        print("--------------------")
        print(f"总收入：{total_income:.2f} 元")
        print(f"总支出：{total_expense:.2f} 元")
        print(f"余额：{balance:.2f} 元")

    elif action == "退出":
        print("记账本已关闭，再见！")
        break

    else:
        print("操作不正确，请输入：添加、查看 或 退出。")
