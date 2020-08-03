from Bio import SeqIO

def read_fasta(file):
    G = []
    for record in SeqIO.parse(file, "fasta"):
        #record.id, record.seq
        G.append(str(record.seq))
    return G

def subsequence(T,P):
    i = 0
    m = len(P)
    pos = []
    for j in range(len(T)):
        if T[j] == P[i]:
            pos.append(j+1)
            i+=1
        if i == m:
            break
    return pos


fasta = read_fasta("./rosalind_sseq.txt")
T = fasta[0]
P = fasta[1]
sub = subsequence(T,P)

for s in sub:
    print(s, end=" ")
