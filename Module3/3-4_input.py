# input() 函數 讓使用者在終端機輸入資料

# 取得使用者輸入的資料
user_input = input("請輸入數字：")
print(user_input)
print(type(user_input))


# 將使用者輸入強制轉型成 int
user_input = int(input("請輸入數字："))
print(type(user_input))
if user_input > 10:
    print("num 大於 10")
