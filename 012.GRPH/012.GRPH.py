from Bio import SeqIO

G = []
for record in SeqIO.parse("./rosalind_grph.txt", "fasta"):
    G.append([str(record.id), str(record.seq)])


k = 3
for i in range(len(G)):
    for j in range(len(G)):
        if i != j and G[j][1][:k] == G[i][1][len(G[i][1])-k:]:
            print(G[i][0],G[j][0])


