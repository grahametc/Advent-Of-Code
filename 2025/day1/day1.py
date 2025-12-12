f = open("input.txt")

sum = 50
count1=0
count2=0


for line in f:
    
    if line.startswith("R"):
        for j in range(0, int(line[1:(len(line))])):
            sum+=1
            if sum % 100 == 0:
                count2+=1


    if line.startswith("L"):
        for i in range(0, int(line[1:(len(line))])):
            sum-=1
            if sum % 100 == 0:
                count2+=1
    
    if sum %100 == 0:
        count1+=1
    line_num+=1


print("Zero Count:"+str(count1))
print("Rotation Zero Count:" + str(count2))