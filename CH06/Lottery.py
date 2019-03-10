import random

lottery_ticket = set()
while len(lottery_ticket) < 7:
    number = random.randint(1, 48)
    lottery_ticket.add(number)

for single_number in lottery_ticket:
    print(single_number)