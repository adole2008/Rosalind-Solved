#Solution for Overlap Graphs (link: https://rosalind.info/problems/grph/)
# O(n^2) time complexity >>>> (i'm so cooked)

def main():
    dna_dict = {}
    key = ""
    val = ""
    with open("rosalind_grph.txt", "r") as f:
        for line in f:
            if line[0] == ">":
                dna_dict[key] = val
                key = line[1:].strip()
                dna_dict[key] = ""
                val = ""
            else:
                val += line.strip()
        dna_dict[key] = val

    tuples = compare(dna_dict)
    for a,b in tuples:
        print(a, b)

def compare(d):
    l = list(d.keys())
    return_val = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if d[l[i]][-3:] == d[l[j]][:3]:
                # Relation between LIST[i] -> LIST[j]
                comparison = (l[i], l[j])
                return_val.append(comparison)
            if d[l[j]][-3:] == d[l[i]][:3]:
                #Relation between LIST[j] -> LIST[i]
                comparison = (l[j], l[i])
                return_val.append(comparison)
    return return_val

if __name__ == "__main__":
    main()