from Bio import SeqIO

def consensus(G):
    m = len(G[0])

    pro = {'A': [0] * m,
           'C': [0] * m,
           'G': [0] * m,
           'T': [0] * m}

    for g in G:
        for i in range(m):
            pro[g[i]][i] += 1

    con = ""
    for i in range(m):
        most_f = 0
        a = "A"
        for k in pro.keys():
            if pro[k][i] > most_f:
                most_f = pro[k][i]
                a = k
        con += a
    print(con)
    for k in pro.keys():
        print(k,": ", sep="", end="")
        for i in range(m):
            end = " "
            if i == m-1:
                end = ""
            print(pro[k][i], end=end)
        print()



G = []
for record in SeqIO.parse("./rosalind_cons.txt", "fasta"):
    G.append(str(record.seq))

consensus(G)
