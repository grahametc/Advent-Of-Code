with open('input.txt', 'r') as file:
    arr = [line.strip().split() for line in file]

rightArr = [] 
leftArr = [] 
for i in range(0, len(arr)):
    leftArr.append(int(arr[i][0]))
    rightArr.append(int(arr[i][1]))

leftArr.sort()
rightArr.sort()




def dists():
    dist = []
    total = 0
    for j in range(0, len(leftArr)):
        dist.append(abs(leftArr[j] - rightArr[j]))
        total += dist[j]
    print("Total Distance: ")
    print(total)  

def similarity():
    dict = {}
    for d in rightArr:
        if d in dict:
            dict[d] = dict[d] + 1
        else:
            dict[d] = 1
    tot = 0
    for k in leftArr:
        mult = 0
        if k in dict:
            mult = dict[k]
        tot += k * mult
    print("Similarity Score: ")
    print(tot)



dists()
similarity()