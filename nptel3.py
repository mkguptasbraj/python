
def gcd(m, n):
    i = min(m, n)
    while i > 0:
        if m % i == 0 and n % i == 0:
            return i
        else:
            i -= 1
    return i  # This line should be outside the loop

print(gcd(10, 30))  # Should print 10
