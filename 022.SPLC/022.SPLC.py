from queue import Queue
from Bio import SeqIO

class AhoCorasick:
    class Trie():
        class Node():
            def __init__(self, childs, edge, parent, link, leaf):
                self.childs = childs
                self.edge = edge
                self.parent = parent
                self.link = link
                self.leaf = leaf

        def getChild(self, u, c):
            return self.trie[u].childs[c] if (c in self.trie[u].childs) else -1

        def __init__(self, l_str):
            self.trie = []
            self.trie.append(self.Node({}, '0', 0, 0, -1))
            #print(l_str)

            m = len(l_str)
            for j in range(m):
                u = 0
                T = l_str[j]
                i = 0

                # Match string
                v = self.getChild(u, T[i])
                while v != -1:
                    i += 1
                    u = v
                    v = self.getChild(u, T[i])

                # Add string
                while i < len(T):
                    self.trie.append(self.Node({}, T[i], u, 0, -1))
                    nn = len(self.trie) - 1
                    self.trie[u].childs[T[i]] = nn
                    u = nn
                    i += 1
                self.trie[u].leaf = j

        def failureLink(self, u):
            if self.trie[u].parent == 0:
                self.trie[u].link = 0
            else:

                c = self.trie[u].edge
                p = self.trie[u].parent
                l = self.trie[p].link
                v = self.getChild(l, c)
                while l != 0 and v == -1:
                    l = self.trie[l].link
                    v = self.getChild(l, c)

                v = self.getChild(l, c)
                if v != -1:
                    self.trie[u].link = v
                else:
                    self.trie[u].link = 0

        def createSuffixLink(self):
            n = len(self.trie)
            visited = [False] * n
            q = Queue()
            q.put(0)
            #print(0)
            while not q.empty():
                u = q.get(0)
                for v in self.trie[u].childs.values():
                    if not visited[v]:
                        #print(v, end=" ")
                        q.put(v)
                self.failureLink(u)
            #print()

        def print(self):
            i = 0
            for u in self.trie:
                print(i, u.edge,u.parent,u.link)
                i+=1

        def graphviz(self):
            for u in range(len(self.trie)):
                for v in self.trie[u].childs.values():
                    print(u, "->", v, "[label=", self.trie[v].edge,"]", sep="")

    def __init__(self, T, P):
        tt = self.Trie(P)
        tt.createSuffixLink()
        #trie.print()
        #trie.graphviz()
        n = len(T)
        j = 0
        u = 0
        self.introns = []
        while j < n:
            while j < n and tt.getChild(u, T[j]) != -1:
                u = tt.getChild(u, T[j])
                if tt.trie[u].leaf != -1:
                    #print(j-len(P[tt.trie[u].leaf])+2, tt.trie[u].leaf +1)
                    self.introns.append((j-len(P[tt.trie[u].leaf])+1, j))
                j += 1
            if u == 0:
                j+=1

            u = tt.trie[u].link


def read_fasta(file):
    G = []
    for record in SeqIO.parse(file, "fasta"):
        G.append(str(record.seq))
    return G

def translation(DNA, introns):
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

    n = len(DNA)
    prot = ""
    j = 0
    i = 0
    while i < n-3+1:
        if j < len(introns) and i == introns[j][0]:
            # jump the intron
            i = introns[j][1]+1
            j += 1

        if i < n-3+1:
            AA = rna2prot[DNA[i:i+3]]
            if AA != 'Stop':
                prot += AA
            else:
                i = n
                #break
        i += 3
    return prot


fasta = read_fasta("./rosalind_splc.txt")
T = fasta[0]
P = fasta[1:]
#P = ["banana", "anna", "naan", "ananas", "abandon"]
#T = "bannabanana"
ac = AhoCorasick(T,P)
#print(ac.introns)
print(translation(T,ac.introns))

