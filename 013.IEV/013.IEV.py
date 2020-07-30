with open("./rosalind_iev.txt") as f:
    l = f.readline().strip().split(" ")

p = [float(i) for i in l]


P = [1., 1., 1., 3/4, 1/2, 0.]

off = 0
for i in range(len(P)):
    off += 2.0 * P[i]*p[i]

print(off)

