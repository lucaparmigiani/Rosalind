import requests
from Bio import SeqIO

url = 'https://www.uniprot.org/uniprot/B5ZC00.fasta'

res = requests.get(url)
f = res.content

for record in SeqIO.parse(f[2:], "fasta"):
    a = str(record.seq)
