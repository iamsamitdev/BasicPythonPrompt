numbers = {1: "One", 2: "Two", 3: "Three"}

province = {
    "bkk": "Bangkok",
    "cha": "Chiang Mai",
    "knn": "Khon Kaen",
    "nkh": "Nakhon Ratchasima"
}

print(numbers)
print(numbers[1])
print(numbers[3])

print("--------------------")

print(province["bkk"])

print("--------------------")

# loop dictionary
for p in province:
    print(p)

print("--------------------")

for p in province.values():
    print(p)

print("--------------------")

for k, p in province.items():
    print(k, p)
