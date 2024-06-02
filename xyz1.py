def power (x,n):
    ans = 1
    for i in range (0,n):
        ans = ans*x
    return (ans)
print(power(2,5))