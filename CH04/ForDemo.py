name_list = ["Amy", "Bob", "Carol"]

for single_name in name_list:
    print(single_name)

print("---------------------")

name_set = {"Amy", "Bob", "Carol", "Amy"}
for single_name in name_set:
    print(single_name)

print("---------------------")

ppl_info = {"name": "Elwing", "height": 175, "weight": 75}

for single_key in ppl_info:
    print(single_key, ppl_info[single_key])

print("---------------------")

for single_number in range(0, 9):
    print(single_number + 1)

print("---------------------")

result = 0
for single_number in range(0, 10):
    result = result + (single_number + 1)
print("result =", result)