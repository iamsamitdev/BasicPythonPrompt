for i in range(1, 11):
    if i == 10:
        print(i, end="")
    else:
        print(i, end=",")
print("\n--------------------")

for j in range(1, 101):
    if j % 10 == 0:
        print(f"{j:03}")
    else:
        print(f"{j:03}", end=" ")
