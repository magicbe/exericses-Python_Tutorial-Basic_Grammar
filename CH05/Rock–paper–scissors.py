import random

choice = int(input("請出拳 [0]剪刀 [1]石頭 [2]布"))
print("你的出拳", choice)
com_choice = random.randint(0, 2)
print("電腦的出拳", com_choice)

if choice == (com_choice + 1) % 3:
    print("你贏了")
elif choice == com_choice:
    print("平手")
else:
    print("你輸了")