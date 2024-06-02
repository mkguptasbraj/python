def gcd(m,n):
 i = min(m,n)   
 while i>0:
  if (m%i==0) and (n%i==0):
    return(i)
 else :
   return i -1
 return i  
 
gcd(10,30)
