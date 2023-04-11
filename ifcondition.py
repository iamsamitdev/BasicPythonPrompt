# level = 2
# alive = False

# if level == 1 and alive == True:
#     print("You are at level 1")
# elif level == 2 and alive == True:
#     print("You are at level 2")
# else:
#     print("You are not alive")

# รับค่าจากผู้ใช้
level = input("Enter game level (1-3): ")
# print("Hello", fname)

# check type
# print(type(fname))
if level == "1":
    print("You are at level 1")
elif level == "2":
    print("You are at level 2")
elif level == "3":
    print("You are at level 3")
else:
    print("You are not select level")
