# example of data: Ali 90 90 70 50
'''
try:
    results = []  # Store the results in memory
    with open("input.txt") as file:
        for line in file:
            grades = line.split()
            if len(grades) == 5:
                result = (int(grades[1]) + int(grades[2])) *0.15 + int(grades[3]) * 0.30 + int(grades[4]) * 0.40
                if result >= 60:
                    results.append([grades[0], "has passed this course."])
                else:
                    results.append([grades[0], "has failed in this course"])
            else:
                raise ValueError("Invalid grade format: " + line)

    # If no errors occurred during processing, print all results
    for name, message in results:
        print(name, message)

except (FileNotFoundError, ValueError) as e:
    print("An error occurred:", str(e))
    print("No results were printed due to errors.")
'''
# example of data: 712,9.8
'''
try:
    with open("input.txt") as file:
        lines = file.readlines()
        sum = 0
        avg = 0
        for line in lines:
            information = line.split(",")
            sum += float(information[1])
        avg = sum/len(lines)
    with open("output.txt",'w') as output:
        output.write(f"Average {avg:0.5}")
        output.write(f" students below avg: \n")
        for line in lines:
            information = line.split(",")
            if(float(information[1]) < avg):
                output.write(f"{information[0]}\n")
            
except Exception as e:
    print("Error bro!" , e)
'''
        

            