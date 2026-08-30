#for loop
for i in range(1, 6):
    print(i)



#whie loop 
count = 1

while count <= 5:
    print(count)
    count += 1

#range()
for i in range(5):
    print(i)


#ranege with start and end
for i in range(2, 21, 2):
    print(i)


#range with start, end and step
for i in range(10, 0, -1):
    print(i)


#break statement
for i in range(1, 11):
    if i == 6:
        break
    print(i)


#continue statement
for i in range(1, 11):
    if i == 6:
        continue
    print(i)