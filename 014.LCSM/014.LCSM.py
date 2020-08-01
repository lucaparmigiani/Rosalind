from unicodedata import *
import random
from Bio import SeqIO

#for x in xlist:
#    if name(x,'-')!='-':
#        print(x,'|', "%04x"%(ord(x)), '|', name(x,'-'), "|", 'a' < x)

class GeneralSuffixTree():
    class Node():
        def __init__(self, childs, parent, sd, leaf, link, string):
            self.childs = childs
            self.parent = parent
            self.sd = sd
            self.leaf = leaf
            self.link = link
            self.string = string

    def getChild(self, u, c):
        return self.tree[u].childs[c] if (c in self.tree[u].childs) else -1

    def suffixLink(self, u, l_str, j):
        self.str = l_str
        T = l_str[j]
        if self.tree[u].sd <= 1:
            self.tree[u].link = 0
        else:
            f = self.tree[self.tree[u].parent].link
            c = ""
            while self.tree[f].sd < self.tree[u].sd - 1:
                c = T[self.tree[u].leaf + self.tree[f].sd + 1]
                #c = T[self.tree[u].leaf + self.tree[f].sd + 1]
                f = self.getChild(f, c)

            if self.tree[f].sd > self.tree[u].sd -1:
                d = self.tree[u].sd - 1
                self.tree.append(self.Node({}, self.tree[f].parent, d, self.tree[u].leaf + 1, -1, j))
                nn = len(self.tree) - 1
                self.tree[nn].childs[l_str[self.tree[f].string][self.tree[f].leaf+d]] = f

                # Modify child of node above
                self.tree[self.tree[f].parent].childs[c] = nn
                # Modify parent of node below
                self.tree[f].parent = nn

                f = nn
            self.tree[u].link = f


    def __init__(self, l_str):
        #unicode characters
        xlist=[]
        k = 0
        for i in range(945, 945 + len(l_str)):
            #xlist.append(eval('u"\\u%04x"' % i))
            l_str[k] = l_str[k] + eval('u"\\u%04x"' % i)
            k += 1
        print(l_str)

        self.tree = []
        self.tree.append(self.Node({}, -1, 0, 0, 0, 0))
        for j in range(len(l_str)):
            T = l_str[j]
            n = len(T)
            u = 0
            d = 0
            for i in range(n):
                # Save this to modify child of node above
                c = T[i+d]
                v = self.getChild(u, c)
                while d == self.tree[u].sd and v != -1:
                    c = T[i+d]
                    d += 1
                    u = v
                    while self.tree[u].sd > d and T[i+d] == l_str[self.tree[u].string][self.tree[u].leaf + d]:
                        d += 1
                    v = self.getChild(u,T[i+d])

                # we are in locus(u,d)
                if d < self.tree[u].sd:
                    # Create new node
                    self.tree.append(self.Node({}, self.tree[u].parent, d, i, -1, j))
                    nn = len(self.tree) - 1
                    self.tree[nn].childs[l_str[self.tree[u].string][self.tree[u].leaf + d]] = u
                    # Modify child of node above
                    self.tree[self.tree[u].parent].childs[c] = nn
                    # Modify parent of node below
                    self.tree[u].parent = nn

                    u = nn

                if self.tree[u].link == -1:
                    self.suffixLink(u, l_str, j)
                # Insert non matched suffix
                self.tree.append(self.Node({}, u, n-i, i, -1, j))
                self.tree[u].childs[T[i+d]] = len(self.tree) - 1

                # Restart
                u = self.tree[u].link
                d = self.tree[u].sd
                #u = 0
                #d = 0

    def print(self):
        for x in self.tree:
            print(T[x.string][x.leaf : x.leaf+x.sd], "\t", x.parent, sep="")

    def graphviz(self, l_str):
        for u in range(len(self.tree)):
            #print(u, self.tree[u].childs)
            for v in self.tree[u].childs.values():
                i = self.tree[v].leaf + self.tree[u].sd
                print(u, "->", v, "[label=", l_str[self.tree[v].string][i : i + self.tree[v].sd - self.tree[u].sd ],"]", sep="")

    def recLCF(self, u):
        node = self.tree[u]
        if len(node.childs) == 0:
            return {node.string}
        s = set()
        for v in node.childs.values():
            s = s.union(self.recLCF(v))
        if len(s) == len(self.str):
            if node.sd > self.m:
                self.m = node.sd
                self.lcf = self.str[node.string][node.leaf:node.leaf+node.sd]
        return s

    def LCF(self):
        n = len(self.tree)
        self.m = 0
        self.lcf = ""
        self.recLCF(0)
        print(self.lcf)

def read_set(file):
    G = []
    for record in SeqIO.parse(file, "fasta"):
        #record.id, record.seq
        G.append(str(record.seq))
    return G

if __name__ == "__main__":
    T = read_set("./rosalind_lcsm.txt")
    ST = GeneralSuffixTree(T)
    ST.LCF()
    #ST.print()
    #print(30*'*')
    #ST.graphviz(T)


#T = ['GATTACA', 'TAGACCA', 'ATACA']
#T = []
#for i in range(10):
#    x = ""
#    for j in range(5):
#        x += random.choice("ACGT")
#    T.append(x)
