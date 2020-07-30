
def max_GC_content_fasta(file):
    GC = 0
    new_GC = 0
    name_GC = '' 

    first = True
    with open(file) as f:
        for line in f:
            if first:
                first = False
                name_GC = line[1:]
                name = name_GC
                count = 0
                GC_count = 0

            else: 
                if line[0] == '>':
                    new_GC = GC_count/count
                    if new_GC > GC:
                        GC = new_GC
                        name_GC = name

                    name = line[1:]
                    count = 0
                    GC_count = 0
                else:
                    for i in line.strip():
                        count += 1
                        if i == 'C' or i == 'G':
                            GC_count += 1

    new_GC = GC_count/count
    if new_GC > GC:
        GC = new_GC
        name_GC = name

    print(name_GC.strip())
    print(GC*100)

max_GC_content_fasta('./rosalind_gc.txt')
