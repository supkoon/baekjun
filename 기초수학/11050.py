def factorial(n):
    if (n==0) or (n==1) :
        return 1
    else: return n*factorial(n-1)

n, k = map(int,input().split())
result =  factorial(n)//(factorial(k)*factorial(n-k))
print(result)

