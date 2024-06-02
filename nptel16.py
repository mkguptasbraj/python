def findpos(l,v):
    found=False
    i=0
    pos = -1
    while i<len(l):
        if(l[i])==v:
            found=True
            pos = i
            break
        i+=1
           
    return(pos)
l = [1,2,3,4,5,53,27,22]
print(findpos(l ,5))