from Bio import SeqIO

def read_s(file):
    G = []
    for record in SeqIO.parse(file, "fasta"):
        G.append([str(record.id), str(record.seq)])

    return G[0][1]


def rev_com(s):
    comp = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    t = ""
    for i in range(len(s)-1,-1,-1):
        t += comp[s[i]]
    return t

s = read_s("./rosalind_revp.txt")
print(s)
print(rev_com(s))

Min = 4
Max = 13 # <-- remeber this piece of sh..
for i in range(len(s)-Min + 1):
    for j in range(Min, min(Max, len(s)-i+1)):
        if s[i:i+j] == rev_com(s[i:i+j]):
            print(i+1, j, sep = '\t')

print(len(s))
