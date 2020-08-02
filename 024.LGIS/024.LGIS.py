# Dynamic programming solution
# TODO: do this in O(NlogN)

def long_inc_dec_subseq(pi, inc = True):

    n = len(pi)
    D = [1] * n
    m = 0
    for i in range(1,n):
        tmp = 1
        for j in range(i):
            if inc:
                if pi[i] > pi[j]:
                    tmp = max(tmp, D[j] + 1)
            else: 
                if pi[i] < pi[j]:
                    tmp = max(tmp, D[j] + 1)
        if tmp > m:
            m = tmp
            idx = i
        D[i] = tmp

    i = idx
    lis = [None] * m
    while i >= 0 and m > 0:
        if D[i] == m:
            lis[m-1] = pi[i]
            m -= 1
        i-=1
    return lis

with open('./rosalind_lgis.txt') as f:
    n = int(f.readline().strip())
    pi = f.readline().strip().split(' ')

pi = [int(i) for i in pi]
#pi = [3, 8, 9, 4, 5, 1, 6, 7]
lis = long_inc_dec_subseq(pi, inc = True)
lds = long_inc_dec_subseq(pi, inc = False)

for i in lis:
    print(i, end=" ")
print()
for i in lds:
    print(i, end=" ")
