#Solution to Consensus and Profile (link: https://rosalind.info/problems/cons/)

def main():
    dna = []

    append_str =""
    with open("rosalind_cons.txt", "r") as f:
        for line in f:
            if line[0] == ">":
                dna.append(append_str)
                append_str = ""
            else:
                line = line.strip()
                append_str += line
        dna.append(append_str)
    dna.remove("")

    values = [0,0,0,0]
    profile_mat = []

    dna = [list(row) for row in zip(*dna)]

    for row in dna:
        values[0] = sum(1 for e in row if e == "A")
        values[1] = sum(1 for e in row if e == "C")
        values[2] = sum(1 for e in row if e == "G")
        values[3] = sum(1 for e in row if e == "T")
        profile_mat.append(values)
        values = [0 for _ in values]
        
    str=""
    bases = ["A", "C", "G", "T"]

    for freq in profile_mat:
        str += bases[freq.index(max(freq))]
        
    print(str)
    profile_mat = [list(row) for row in zip(*profile_mat)]
    print("A: ", end="")
    print(*[i for i in profile_mat[0]], sep=" ")
    print("C: ", end="")
    print(*[i for i in profile_mat[1]], sep=" ")
    print("G: ", end="")
    print(*[i for i in profile_mat[2]], sep=" ")
    print("T: ", end="")
    print(*[i for i in profile_mat[3]], sep=" ")

if __name__ == "__main__":
    main()