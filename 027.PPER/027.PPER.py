mod = 1000000

def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))

def partialPermutation(n,k):
    return int((fact(n)/(fact(n-k)))%mod)

n = 94
k = 8
print(partialPermutation(n,k))
