f = open('./rosalind_rna.txt')

for i in f.read():
    a = i[::-1]
    if a == 'T':
        a = 'U'
    print(a, end='')

