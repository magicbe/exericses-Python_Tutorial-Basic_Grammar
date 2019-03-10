from PasswordMachine import Machine

min = int(input("請使用者輸入你想要的下限："))
max = int(input("請使用者輸入你想要的上限："))

mach = Machine(min, max)

while True:
    interval = mach.returnInterval()
    msg = "請輸入[" + str(interval[0]) + "-" + str(interval[1]) + "]的數字："
    n = int(input(msg))
    if mach.guess(n) == True:
        break

print("你猜對了！總共猜了", mach.guess_times, "次")