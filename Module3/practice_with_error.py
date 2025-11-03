# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」
print("""歡迎來到猜數字遊戲
我將選擇一個 1 到 100 之間的整數，你來試著猜中它!""")

import random
prompt = "請猜一個 1 ~ 100 之間的正整數:"
answer = random.randint(1, 100)

while True:
    try:
        user_input = int(input(prompt))
    except KeyboardInterrupt:
        print(f"\n遊戲被手動終止，答案其實是 {answer}，歡迎下次再挑戰!")
        break
    except:
        prompt = "您的輸入不符合要求，罰您重看題目！\n請輸入符合要求的內容："
        continue
    if user_input < 1 or user_input > 100:
        prompt = "超出範圍，請重新輸入："
    elif user_input > answer:
        prompt = "請輸入更小的數字："
    elif user_input < answer:
        prompt = "請輸入更大的數字："
    else:
        print("恭喜中獎!")
        break