from Bio import SeqIO
from operator import itemgetter

def computeBorder(s):
    pi = [None for i in range(len(s))]
    pi[0] = -1
    k = -1
    for i in range(1,len(s)):
        while k >= 0 and s[i] != s[k + 1]:
            k = pi[k]
        if s[i] == s[k + 1]:
            k = k + 1
        pi[i] = k
    return pi

def KMP(T,P):
    pi = computeBorder(P)
    #print(pi)

    n = len(T)
    m = len(P)
    res = []

    i = -1
    for j in range(n):
        while i >= 0 and P[i+1] != T[j]:
            i = pi[i]
            if j + m - i  > n:
                break

        if P[i+1] == T[j]:
            i = i + 1
        if i == m-1:
            #print(j - m + 1)
            res.append(j - m + 1)
            i = pi[i]
            if j + m - i  > n:
                break

    return res

def overlap(T,P):
    pi = computeBorder(P)
    #print(pi)

    n = len(T)
    m = len(P)
    res = 0 

    i = -1
    for j in range(n):
        while i >= 0 and P[i+1] != T[j]:
            i = pi[i]
        if P[i+1] == T[j]:
            i = i + 1
        if j == n-1:
            res = i + 1
        # Prevent substring
        if i == m - 1:
            i = pi[i]
    return res

def read_set(file):
    G = []
    for record in SeqIO.parse(file, "fasta"):
        #record.id, record.seq
        G.append(str(record.seq))
    return G

def compute_overlap_graph(S, sort = True):
    n = len(S)
    E = []
    for i in range(n):
        for j in range(n):
            if i != j:
                pref = overlap(S[i],S[j])
                if pref != 0:
                    E.append([i, j, pref])

    if sort:
        return sorted(E, key=itemgetter(2), reverse=True)
    else:
        return E

def check(S, supastring):
    print("Checking superstring...")
    for i in range(len(S)):
        idx = KMP(supastring, S[i])
        if not idx:
            print("*"*30)
            print(i)
            print("no good")
            print("*"*30)
            return
    print("Good")


S = read_set("./rosalind_long.txt")
S_copy = S
print(S)
# THIS DOESN'T WORK
# -----------------------------------------
# This works under the assumption:
# join strings which have overlap > half of
# the len(S[u]) and len(S[v])
# -----------------------------------------
while len(S) > 1:
    n = len(S)
    print(n)
    S_new = []
    print("computing...")
    E = compute_overlap_graph(S, sort=False)
    added = [False for _ in range(n)]
    for e in E:
        u = e[0]
        v = e[1]
        over = e[2]
        if int(len(S[u])/2) < over > int(len(S[v])/2) and \
           not added[u] and not added[v]:
            S_new.append(S[u] + S[v][over:])
            added[u] = True
            added[v] = True
    S = S_new
print(S[0])
check(S_copy, S[0])

# NEEDS TO BE CHECK:
# -----------------------------------------
# 4-approximation for longest superstring
# -----------------------------------------
#i = 0
#n = len(S)
#while i < n - 1:
#    print(i)
#    E = compute_overlap_graph(S)
#    u = E[0][0]
#    v = E[0][1]
#    over = E[0][2]
#    S[u] = S[u] + S[v][over:]
#    S.pop(v)
#    i+=1
#print(S[0])
#check(S_copy, S[0])
