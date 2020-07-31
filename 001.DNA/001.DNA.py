f = open('./rosalind_dna.txt')

dict = {'A':0, 'C':0, 'G':0, 'T':0}
for i in f.read():
    a = i[::-1]
    print(a)
    if(a in dict):
        dict[a] += 1

print(dict)
