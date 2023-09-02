i = 0


equal = 0
for i in range(1, 10):
    if i%2 == 0:
        print(f"{i} is a even number")
        equal += i
        print(equal)


# ---------------- problem 2 Q1 ----------------

name = ["joe", "harlem", "charlie"]
name = [i.title() for i in name]
print(name)