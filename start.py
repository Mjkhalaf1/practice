lst1  = [2,6,3,5,1,10,1,0,50]
tempLst = [0] * (max(lst1)+1)
for i in lst1:
    tempLst[i] +=1
for i in range(1,len(tempLst)):
    tempLst[i] += tempLst[i-1]
sortList = [0] * len(lst1)
for i in reversed(lst1):
    sortedPosition = tempLst[i] - 1
    sortList[sortedPosition] = i
    tempLst[i] -= 1
print(sortList)

lst1  = [2,6,3,5,1,10,1,50,0]
for i in range(1,len(lst1)):
    j = i
    while(lst1[j] < lst1[j-1] and j >= 1):
        lst1[j] , lst1[j-1] = lst1[j-1] , lst1[j]
        j -= 1
print(lst1)

def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))

def palindrome(word, i, j):
    if i > j:
        return True
    else:
        if(word[i] != word[j]):
            return False
        else:
            return palindrome(word , i+1 , j-1)
print(palindrome('racecar' , 0 , 6))

def power(x,n):
    if n==0:
        return 1
    else:
        return x * power(x,n-1)
print(power(10,3))

def sum(lst , i ,j):
    if(i==j):
        return lst[i]
    else:
        return lst[i] + sum(lst,i+1,j)
print(sum([10,25,35,40,15,15] , 0 , 5))

def bin(lst, i, j, v):
    if i > j:
        return -1  
    mid = int((i + j) / 2)
    if lst[mid] == v:
        return mid
    elif lst[mid] > v:
        return bin(lst, i, mid - 1, v)
    else:
        return bin(lst, mid + 1, j, v)

print(bin([1, 2, 3, 4, 5], 0, 4, 5))
print("for odd numbers")
def oddSum(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 1:
            return n + oddSum(n-1)
        else:
            return oddSum(n-1)
print(oddSum(9))