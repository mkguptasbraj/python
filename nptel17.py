def search(seq,v):
    for x in seq:
        if x==v:
            return(True)
    return(False)

seq = [11,22,89,1,3,2,8,3]
print(search(seq,1))