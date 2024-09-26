# A program to recognize the letter on the image between A, C and M??????????????????????????!!
from PIL import Image
images_paths = ["Aorg.png" , "Morg.png" , "Corg.png" , "Test4.png"]  
PxList = []
for imgPath in images_paths:
    image = Image.open(imgPath)
    image = image.convert("RGB")
    width, height = image.size
    BlackList = [0] * 5
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))  
            if (r, g, b) == (0, 0, 0):
                match y:
                    case value if value < height/5:
                        BlackList[0] += 1
                    case value if value < height/4:
                        BlackList[1] += 1
                    case value if value < height/3:
                        BlackList[2] += 1
                    case value if value < height/2:
                        BlackList[3] += 1
                    case value if value < height:
                        BlackList[4] += 1
                
    PxList.append(BlackList)
values = [0] * 3
for i,j in enumerate(PxList):
    if i == 3:
        break
    else:
        summ = 0
        for k in range(len(j)):
            summ = summ +  abs(j[k] - PxList[3][k])
        values[i] = summ
    
Closest = min(values)
indexClosest = values.index(Closest)
if indexClosest == 0:
    print("You wrote the letter A")
elif indexClosest == 1:
    print("You wrote the letter M")
else:
    print("You wrote the letter C")    
        
    