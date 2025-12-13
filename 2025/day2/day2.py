##########################################1########################################
f=open("input.txt")
ids = f.read().replace('\n', '').split(",")
sum1=0
for id in ids:
    for i in range(int(id[0:id.index("-")]), int(id[id.index("-")+1:len(id)])+1):
        strng=str(i)
        if len(strng) % 2 != 0:
            continue
        if(len(strng)==2):
            left=strng[0]
            right=strng[1]
        else:
            left = strng[0:len(strng)//2]
            right = strng[len(strng)//2:len(strng)]
        if left == right:
            sum1+=i
print("Part 1 sum of Invalid IDS:" + str(sum1))
##########################################2########################################

def subs_list(string, n):
    ret = []
    for i in range(0, len(string), n):
        ret.append(string[i:i+n])
    return ret

sum2=0
seen = {}
in_range=False
for id in ids:
    for z in range(int(id[0:id.index("-")]), int(id[id.index("-")+1:len(id)])+1):
        if z < 10: continue
        # duplicates
        if z in seen: continue
        seen[z]=True
        strng2=str(z)
        if(len(strng2)==2):
            if strng2[0] == strng2[1]:
                sum2+=int(strng2)
                continue
        
        dict = {}
        for j in range(0, len(strng2)):
            if(strng2[j]) not in dict:
                dict[strng2[j]]=1
            else:
                dict[strng2[j]]+=1
        if(len(dict)==1): 
            sum2+=int(strng2)
            
            continue
        
        
        for k in range(2, len(strng2) // 2 + 1):
            if len(strng2) % k == 0:
                subs = subs_list(strng2, k)
                
                prev=subs[0]
                eq = True
                for sub in subs:

                    current=sub
                    if current != prev:
                        eq = False
                        break
                    prev=current
                if eq:
                    sum2+=int(strng2)
                    break
print("Part 2 sum of invalid IDS:" + str(sum2))