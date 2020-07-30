def ham(s,t):
    # s and t must have same size
    if len(s) != len(t):
        print("Error, s and t do not have equal size, exit")
        return

    l = len(s)
    dist = 0
    for i in range(l):
        if(s[i] != t[i]):
            dist += 1
    return dist

f = open('./rosalind_hamm.txt')
s = f.readline()
t = f.readline()
print(ham(s,t))
