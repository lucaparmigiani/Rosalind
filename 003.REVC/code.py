f = open('./rosalind_revc.txt')

comp = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
sc = ''
for i in f.read():
    a = i.strip()
    if (a in comp):
        sc += comp[a]

print(sc[::-1])

