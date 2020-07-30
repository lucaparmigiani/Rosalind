# This problem is garbage.
# waste more time on understanding this problem
# than doing all the other exercise

def fib(n,k):
    f1 = 1
    f2 = 1
    for i in range(n-2):
        tmp = f1 + f2*k
        f2 = f1
        f1 = tmp
    return f1

f = open('./rosalind_fib.txt')

l = f.readline().strip().split(' ')
n = int(l[0])
k = int(l[1])
print(n,k)
print(fib(n,k))
