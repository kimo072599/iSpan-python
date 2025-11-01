# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」

user_input = int(input("請輸入 1 ~ 100 之間的正整數:"))
answer = 5

while user_input != answer:
    if user_input < 1 or user_input > 100:
        user_input = int(input("超出範圍，請重新輸入："))
    elif user_input > answer:
        user_input = int(input("請輸入更小的數字："))
    elif user_input < answer:
        user_input = int(input("請輸入更大的數字："))
    else:
        break

print("恭喜中獎")











