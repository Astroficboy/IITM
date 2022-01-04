def prime(n):
    result = True
    for i in range(2, n):
        if (n%i) == 0:
            result = False
            break
    return(result)

def Twin_Primes(n ,m):
    lastprime = 2
    lst = []
    for i in range(min(n, m+1), max(n, m+1)):
        if prime(i):
            d = i - lastprime
            if d == 2:
                lst.append((min(lastprime, i), max(lastprime, i)))
            lastprime = i
    
    return lst
    
    
n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))
