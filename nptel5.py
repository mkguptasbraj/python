#euclid algorithm
def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if(m%n==0):
        return(n)
    else:
        diff =m-n
    return gcd(max(n,diff),min(n,diff))

print(gcd(15,20))
