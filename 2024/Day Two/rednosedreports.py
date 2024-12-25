with open('input.txt', 'r') as file:
    arr = [line.strip().split() for line in file]
#make em ints
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = int(arr[i][j])
print(arr)

def logicalProgression(i):
    increasing = False
    decreasing = False
    for j in range (0, len(arr[i])-1):
        if(arr[i][j] > arr[i][j+1]):
            decreasing = True
            if(increasing):
                return False
        if(arr[i][j] < arr[i][j+1]):
            increasing = True
            if(decreasing):
                return False
        if(arr[i][j] == arr[i][j+1]):
            return False
    return True

def safeDiff(i):
    diff = 0
    safe = False
    for j in range(len(arr[i])-1):
        diff = abs(arr[i][j] - arr[i][j+1])
        if(diff > 3 or diff < 1):
            safe = False
            break
        else:
            safe = True
    return(safe)

def isSafe():
    safeCount = 0
    for i in range(0, len(arr)):
        if(logicalProgression(i) and safeDiff(i)):
            safeCount += 1
            print(i)
    print("Safe Count: ")
    print(safeCount)

isSafe()


