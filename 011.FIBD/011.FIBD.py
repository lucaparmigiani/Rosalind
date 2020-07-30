def fib(n,k):
    f1 = 1
    f2 = 1
    die = [0] * n
    die[0] = f1
    die[1] = f2

    for i in range(2,n):
        tmp = f1 + f2
        if i+1 > k:
            tmp -= die[i-k]
        f2 = f1
        f1 = tmp
        die[i] = f2
    return f1

n = 82
k = 16
print(fib(n,k))
