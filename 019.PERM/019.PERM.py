import itertools

def fact(n):
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)

def perm(a, n):
    for i in itertools.permutations(a, n):
        for j in range(n):
            print(i[j], end= '')
            if(j < n-1):
                print(" ", end= '')

        print()
n = 5
a = [i+1 for i in range(n)]
print(fact(n))
perm(a, n)
