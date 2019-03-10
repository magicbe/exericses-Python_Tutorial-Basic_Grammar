# 不定參數
def add(*args, **kwargs):
    result = 0
    for single_number in args:
        result = result + single_number
    if "mul" in kwargs:
        result = result * kwargs["mul"]
    if "plus" in kwargs:
        result = result + kwargs["plus"]
    return  result

print("result", add(3, 4, 5, 6, 7, 8, 9))
print(add(3, 4, 5, mul=3, plus=5.2))