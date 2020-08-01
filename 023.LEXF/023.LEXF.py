def add_one_base_sigma(base_sigma, sigma):
    base_sigma[0] = (base_sigma[0] + 1) % sigma
    i = 0
    n = len(base_sigma)
    while i < n and base_sigma[i] == 0:
        i += 1
        if i < n:
         base_sigma[i] = (base_sigma[i] + 1) % sigma

    return i >= n

def genComb(alph, n):
    sigma = len(alph)
    base_sigma = [0] * n
    stop = False
    while not stop:
        for j in range(n)[::-1]:
            print(alph[base_sigma[j]], end="")
        print()
        stop = add_one_base_sigma(base_sigma, sigma)

with open('./rosalind_lexf.txt') as f:
    alph = f.readline().strip().split(" ")
    n = int(f.readline().strip())

genComb(alph, n)
