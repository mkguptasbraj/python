def function(n):
    flist =[]
    for i in range (1,n+1):
        if n %i ==0:
            flist = flist +[i]
    return(flist)
print(function(5))
print(function(50))