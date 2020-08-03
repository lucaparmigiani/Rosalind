from Bio import SeqIO

def read_fasta(file):
    G = []
    for record in SeqIO.parse(file, "fasta"):
        #record.id, record.seq
        G.append(str(record.seq))
    return G

def transition_transvertion_ratio(s1,s2):
    transtion_type = {"AG","GA","CT","TC"}
    n = len(s1)
    transition = 0
    transvertion = 0
    for i in range(n):
        if s1[i] != s2[i]:
            if s1[i] + s2[i] in transtion_type:
                transition += 1
            else:
                transvertion += 1
    return transition/transvertion

fasta = read_fasta("./rosalind_tran.txt")
s1 = fasta[0]
s2 = fasta[1]

print(transition_transvertion_ratio(s1,s2))
