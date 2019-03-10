name_set = {"Amy", "Bob", "Carol", "Amy"}
print(name_set)
print("Amy" in name_set)
print(len(name_set))

name_set.add("Emily")
print(name_set)

name_set.remove("Amy")
print(name_set)

name_set.discard("Bob")
print(name_set)

print(name_set.union({"Aaron", "Cammy", "Emily"}))