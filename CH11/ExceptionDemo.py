while True:
    try:
        number = int(input("請輸入整數："))
        break
    except ValueError:
        print("請輸入正確的格式")

print("你輸入對了", number)