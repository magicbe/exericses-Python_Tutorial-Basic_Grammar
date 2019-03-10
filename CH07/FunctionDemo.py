def add(num1, num2):
    num3 = num1 + num2
    return num3

result = add(3, 5.2)
print(result)

result = add("hello", "world")
print(result)

print("------------------------")

def prettifyString(s, prefix="\u2660", postfix="\u2660"):
    result = prefix + s + postfix
    return result

print(prettifyString("hello", "\u2663", "\u2661"))
print(prettifyString("hello2", "\u2663"))
print(prettifyString("hello3"))

print(prettifyString("hello4", postfix="\u2661"))

print("------------------------")

test = "heollo"
print(test.replace("l", "A"))
print(test.replace("l", "A", 1))