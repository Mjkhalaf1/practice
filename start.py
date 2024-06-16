a = []
counter = 1
for i in range(4):
    j = 0
    b = []
    while j < 3:
        b.append(counter)
        counter += 1
        j += 1
    a.append(b)
print(a)

x = [[i+j for i in range(1,5)] for j in range(0,17,4)]
print(x)


    