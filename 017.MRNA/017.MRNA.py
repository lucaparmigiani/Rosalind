from itertools import groupby
#prot2rna = {'F'    : 'UUU', 'L' : 'CUU', 'I' : 'AUU', 'V' : 'GUU',
#            'F'    : 'UUC', 'L' : 'CUC', 'I' : 'AUC', 'V' : 'GUC',
#            'L'    : 'UUA', 'L' : 'CUA', 'I' : 'AUA', 'V' : 'GUA',
#            'L'    : 'UUG', 'L' : 'CUG', 'M' : 'AUG', 'V' : 'GUG',
#            'S'    : 'UCU', 'P' : 'CCU', 'T' : 'ACU', 'A' : 'GCU',
#            'S'    : 'UCC', 'P' : 'CCC', 'T' : 'ACC', 'A' : 'GCC',
#            'S'    : 'UCA', 'P' : 'CCA', 'T' : 'ACA', 'A' : 'GCA',
#            'S'    : 'UCG', 'P' : 'CCG', 'T' : 'ACG', 'A' : 'GCG',
#            'Y'    : 'UAU', 'H' : 'CAU', 'N' : 'AAU', 'D' : 'GAU',
#            'Y'    : 'UAC', 'H' : 'CAC', 'N' : 'AAC', 'D' : 'GAC',
#            'Stop' : 'UAA', 'Q' : 'CAA', 'K' : 'AAA', 'E' : 'GAA',
#            'Stop' : 'UAG', 'Q' : 'CAG', 'K' : 'AAG', 'E' : 'GAG',
#            'C'    : 'UGU', 'R' : 'CGU', 'S' : 'AGU', 'G' : 'GGU',
#            'C'    : 'UGC', 'R' : 'CGC', 'S' : 'AGC', 'G' : 'GGC',
#            'Stop' : 'UGA', 'R' : 'CGA', 'R' : 'AGA', 'G' : 'GGA',
#            'W'    : 'UGG', 'R' : 'CGG', 'R' : 'AGG', 'G' : 'GGG'}

a = ['A', 'A', 'A', 'A', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'G', 'G', 'H', 'H', 'I', 'I', 'I', 'K', 'K', 'L', 'L', 'L', 'L', 'L', 'L', 'M', 'N', 'N', 'P', 'P', 'P', 'P', 'Q', 'Q', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'V', 'V', 'V', 'V', 'W', 'Y', 'Y']
s = list(set(a))
s = sorted(s)
freq = [len(list(group)) for key, group in groupby(a)]

prot2rna = dict(zip(s,freq))
print(prot2rna)

def allMRNA(prt):
    count = 1
    mod = 1000000
    for i in range(len(prt)):
        count= (count*prot2rna[prt[i:i+1]]) % mod
    count = (count*3) % mod # 3 stop codon
    return count


with open("./rosalind_mrna.txt") as f:
    prt = f.readline().strip()
    print(prt)

print(allMRNA(prt))
