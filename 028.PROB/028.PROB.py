from math import log10

def prob(S, gc):
    frq = {'A':(1-gc)/2 ,'C':gc/2, 'G':gc/2, 'T':(1-gc)/2 }
    n = len(S)
    p = 1
    for i in range(n):
        p *= frq[S[i]]
    return log10(p)



with open('./rosalind_prob.txt') as f:
    S = f.readline().strip()
    A = f.readline().strip().split(" ")

A = [float(a) for a in A]
print(S)
print(A)


for a in A:
    print("{:.3f}".format(prob(S, a)), end=" ")

