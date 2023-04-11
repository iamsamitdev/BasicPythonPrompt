names = ['John', 'Paul', 'George', 'Ringo']

print(names)

# แสดงผลลัพธ์
print(names[0], names[3])
# print(names[5])

print(names[-1])
print(names[-4])

# update list value
names[0] = 'Janny'
print(names)

# add new value to list
names.append('Bobby')
print(names)
names.insert(0, 'Samit')
print(names)

# remove value from list
names.pop(0)
print(names)

# count list length
print(len(names))

# loop list
for index, name in enumerate(names):
    print(index, name)
