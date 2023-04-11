i = 1

while i <= 10:
    if i == 10:
        print(i, end="")
    else:
        print(i, end=",")
    i = i + 1

print("\n--------------------")

j = 1

while j <= 100:
    if j % 10 == 0:
        print(f"{j:03}")
    else:
        print(f"{j:03}", end=" ")
    j = j + 1
