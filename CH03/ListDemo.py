a = ["Elwing", "Amy", "Bob"]
print(a)

print(a[1])
print(a[0:2])

a = a + ["Carol", "Dyaln"]
print(a)

print(len(a))

del a[1]
print(a)

a.append("Aaron")
print(a)
a.insert(0, "Carol")
print(a)

a.remove("Carol")
print(a)