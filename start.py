# The use of match in STAT assignemnt 3

x = [[] for i in range(0,11)]
list1 = [11, 15, 19, 24, 32, 36, 40, 43, 46, 49,
        60, 61, 64, 66, 69, 70, 73, 77, 79, 78,
        82, 83, 85, 90, 140, 147, 157162, 169,
        184, 205, 249, 264, 288, 323, 389, 512]

for i in list1:
    match i:
        case value if value < 50:
            x[0].append(i)
        case value if value < 100:
            x[1].append(i)
        case value if value < 150:
            x[2].append(i)
        case value if value < 200:
            x[3].append(i)
        case value if value < 250:
            x[4].append(i)
        case value if value < 300:
            x[5].append(i)
        case value if value < 350:
            x[6].append(i)
        case value if value < 400:
            x[7].append(i)
        case value if value < 450:
            x[8].append(i)
        case value if value < 500:
            x[9].append(i)    
        case value if value < 550:
            x[10].append(i)
for i in x:
    print(f"{len(i)} with relative frequency equal: {len(i)/50}")