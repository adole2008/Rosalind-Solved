
def reverse(dna_text):
    reversed_dna = dna_text[::-1]
    return reversed_dna

def complement(dna_text):
    complemented_dna = ""
    for i in dna_text:
        if i == "A":
            complemented_dna += "T"
        elif i == "T":
            complemented_dna += "A"
        elif i == "C":
            complemented_dna += "G"
        elif i == "G":
            complemented_dna += "C"
    return complemented_dna

def main():
    f = open("data.txt", "r")
    dna_text = f.read()
    reverse_complement = complement(reverse(dna_text))
    print(reverse_complement)


if __name__ == "__main__":
    main()
