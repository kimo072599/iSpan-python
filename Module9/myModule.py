def get_discount(total, discount):
    if total >= 2000:
        total -= discount
    #print("結帳金額為：", total - discount)
    return total

print(__name__)


if __name__ == "__main__":
# 測試模組
    data = [
        {
            "total": 6000,
            "discount": 200
        },
        {
            "total": 8000,
            "discount": 200

        }
    ]

    for d in data:
        print(d["total"],d["discount"])
        answer = get_discount(d["total"],d["discount"])
        print(f"折扣後的金額： {answer}元")

