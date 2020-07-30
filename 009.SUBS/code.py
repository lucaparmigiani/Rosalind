f = open('./rosalind_subs.txt')
s = f.readline().strip()
p = f.readline().strip()

n = len(s)
m = len(p)
for i in range(n-m+1):
    if s[i:i+m] == p:
        print(i+1, end = ' ')
