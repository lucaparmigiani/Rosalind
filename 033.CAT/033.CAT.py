from Bio import SeqIO

def read_fasta(filename):
    fasta = []
    for record in SeqIO.parse(filename, "fasta"):
        #record.id, record.seq
        fasta.append(str(record.seq))
    return fasta

# Catalan numbers
def noncrossing_matching(S):
    n = len(S)
    base = {'A':0, 'C':0, 'G':0, 'U':0}
    for i in range(n):
        base[S[i]] += 1
    C = [0] * n
    C[0] = 1
    for i in range(1,n):
        for j in range(i+1):
            C[i] += C[j-1] * C[i-j]

    print(C)

    noncross_match = 1


    

filename = "./data"
fasta = read_fasta(filename)[0]
print(fasta)
noncrossing_matching(fasta)


