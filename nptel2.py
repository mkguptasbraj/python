def gcd(m,n):
    cf=[]
    for i in range(1, min(m,n)+1):
        if(m%i==0) and(n%i)==0 :
         cf.append(i)
    return(cf[-1])

print(gcd(10,20))
print(gcd(200,195))
print(gcd(21,42))
print(gcd(500,501))
