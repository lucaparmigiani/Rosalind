from Bio import SeqIO

def read_fasta(file):
    for record in SeqIO.parse(file, "fasta"):
        #record.id, record.seq
        G = str(record.seq)
    return G

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

fasta = read_fasta("./rosalind_pmch.txt")
n = len(fasta)
frq = {'A':0, 'G':0}
for i in range(n):
    if fasta[i] in frq:
        frq[fasta[i]] += 1
#print(frq)
print(fact(frq['A'])*fact(frq['G']))

