def search(seq,v):
    for x in seq:
        if x == v :
         return(True)
    return(False)

seq = {11,2,11,33,44,55,77,88,9930,0,2}
print(search(seq,11))