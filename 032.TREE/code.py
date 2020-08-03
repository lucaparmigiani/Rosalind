seen = []

def dfs(adj, u):
    global seen
    seen[u] = 1
    for v in adj[u]:
        if not seen[v]:
            dfs(adj, v)

def connect_comp(adj):
    global seen
    n = len(adj)
    seen = [0 for _ in range(n)]
    cnt = 0
    for i in range(n):
        if not seen[i]:
            cnt+=1
            dfs(adj, i)
    return cnt

with open("./rosalind_tree.txt") as f:
    n = int(f.readline().strip())
    print(n)
    adj = [[] for i in range(n)]
    for l in f.readlines():
        line = l.strip().split(' ')
        u = int(line[0]) - 1
        v = int(line[1]) - 1
        adj[u].append(v)
        adj[v].append(u)

#print(adj)
print("Number of edges to add\n", connect_comp(adj) - 1, sep="")
