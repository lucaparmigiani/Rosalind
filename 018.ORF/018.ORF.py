from Bio import SeqIO

rna2prot = {'TTT' : 'F'   , 'CTT' : 'L', 'ATT' : 'I', 'GTT' : 'V',
            'TTC' : 'F'   , 'CTC' : 'L', 'ATC' : 'I', 'GTC' : 'V',
            'TTA' : 'L'   , 'CTA' : 'L', 'ATA' : 'I', 'GTA' : 'V',
            'TTG' : 'L'   , 'CTG' : 'L', 'ATG' : 'M', 'GTG' : 'V',
            'TCT' : 'S'   , 'CCT' : 'P', 'ACT' : 'T', 'GCT' : 'A',
            'TCC' : 'S'   , 'CCC' : 'P', 'ACC' : 'T', 'GCC' : 'A',
            'TCA' : 'S'   , 'CCA' : 'P', 'ACA' : 'T', 'GCA' : 'A',
            'TCG' : 'S'   , 'CCG' : 'P', 'ACG' : 'T', 'GCG' : 'A',
            'TAT' : 'Y'   , 'CAT' : 'H', 'AAT' : 'N', 'GAT' : 'D',
            'TAC' : 'Y'   , 'CAC' : 'H', 'AAC' : 'N', 'GAC' : 'D',
            'TAA' : 'Stop', 'CAA' : 'Q', 'AAA' : 'K', 'GAA' : 'E',
            'TAG' : 'Stop', 'CAG' : 'Q', 'AAG' : 'K', 'GAG' : 'E',
            'TGT' : 'C'   , 'CGT' : 'R', 'AGT' : 'S', 'GGT' : 'G',
            'TGC' : 'C'   , 'CGC' : 'R', 'AGC' : 'S', 'GGC' : 'G',
            'TGA' : 'Stop', 'CGA' : 'R', 'AGA' : 'R', 'GGA' : 'G',
            'TGG' : 'W'   , 'CGG' : 'R', 'AGG' : 'R', 'GGG' : 'G'}

def getCDNA(DNA):
    comp = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    cDNA = ""
    for i in range(len(DNA)):
        cDNA += comp[DNA[i]]
    return(cDNA[::-1])

def ORF(fasta):
    m = len(fasta)
    start = 'ATG'
    orf = []
    for k in range(3):
        stack = 0
        for j in range(k,m-3+1,3):
            if rna2prot[fasta[j:j+3]] == 'Stop':
                stack = 0
            if stack > 0:
                n = len(orf)
                aa = rna2prot[fasta[j:j+3]]
                for i in range(stack):
                    orf[n-i-1] += aa

            if fasta[j:j+3] == start:
                stack += 1
                orf.append("M")
        if stack > 0:
            orf = orf[:-stack]
    return(orf)

for record in SeqIO.parse("./rosalind_orf.txt", "fasta"):
    DNA = str(record.seq)

print(DNA)
cDNA = getCDNA(DNA)
orf = ORF(DNA)
orf2 = ORF(cDNA)
allORF = set(orf).union(set(orf2))
for prt in allORF:
    print(prt)

