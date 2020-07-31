import requests

def isNglicosylation(s):
    return s[0] == 'N' and s[1] != 'P' and \
          (s[2] == 'S' or s[2] == 'T') and \
           s[3] != 'P'

def findNglicosylation(uniprot_id, fasta):
    n = len(fasta)
    nglico = []
    for i in range(n-4+1):
        if isNglicosylation(fasta[i:i+4]):
            nglico.append(i+1)
    if nglico:
        print(uniprot_id)
        for i in range(len(nglico)):
            end = " "
            if i == len(nglico) - 1:
                end = ""
            print(nglico[i], end=end)
        print()


def openFasta(uniprot_id):
    url = 'https://www.uniprot.org/uniprot/' + uniprot_id + ".fasta"
    res = requests.get(url)
    f = str(res.content)[2:-3]
    fs = f.split('\\n')
    fasta = ''.join(fs[1:])
    return fasta



with open('./rosalind_mprt.txt') as f:
    for line in f.readlines():
        uniprot_id = line.strip()
        fasta = openFasta(uniprot_id)
        findNglicosylation(uniprot_id, fasta)
