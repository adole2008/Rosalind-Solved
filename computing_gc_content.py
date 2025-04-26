#Solution to Computing Gc content (link: https://rosalind.info/problems/gc/)

#reverse complement of a DNA strand has the same GC percentage
#prokaryotes have gc content significantly higher than 50%

def cg_percentage(dna):
    total = len(dna)
    cg = dna.count("C") + dna.count("G")
    return (cg/total) * 100

def main():
    dna = {}   
    with open("data.txt", "r") as f:
        count = 0
        current_key = ""
        for line in f:
            if line[0] == '>':
                current_key = line.strip()
                dna[current_key] = ""
            else:
                dna[current_key] += line.strip()
    
    max_cg = 0
    id = ""
    for key, val in dna.items():
        temp = cg_percentage(val)
        if temp > max_cg:
            max_cg = temp
            id = key

    print(id)
    print(max_cg)

if __name__ == "__main__":
    main()
