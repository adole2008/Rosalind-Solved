#Solution to Translating RNA to Protein (link: https://rosalind.info/problems/prot/)

codon_to_amino = {
    "UUU" : "F", "UUC" : "F",
    "UUA" : "L", "UUG" : "L", "CUU" : "L", "CUC" : "L", "CUG" : "L", "CUA" : "L",
    "AUU" : "I", "AUC" : "I", "AUA" : "I",
    "AUG" : "M",
    "GUU" : "V", "GUC" : "V", "GUA" : "V", "GUG" : "V",
    "UCU" : "S", "UCC" : "S", "UCA" : "S", "UCG" : "S", "AGU" : "S", "AGC" : "S",
    "CCU" : "P", "CCC" : "P", "CCA" : "P", "CCG" : "P",
    "ACU" : "T", "ACC" : "T", "ACA" : "T", "ACG" : "T",
    "GCU" : "A", "GCC" : "A", "GCA" : "A", "GCG" : "A",
    "UAU" : "Y", "UAC" : "Y",
    "UAA" : "Stop", "UAG" : "Stop", "UGA" : "Stop",
    "CAU" : "H", "CAC" : "H",
    "CAA" : "Q", "CAG" : "Q",
    "AAU" : "N", "AAC" : "N",
    "AAA" : "K", "AAG" : "K",
    "GAU" : "D", "GAC" : "D",
    "GAA" : "E", "GAG" : "E",
    "UGU" : "C", "UGC" : "C",
    "UGG" : "W",
    "CGU" : "R", "CGC" : "R", "CGA" : "R", "CGG" : "R", "AGA" : "R", "AGG" : "R",
    "GGU" : "G", "GGC" : "G", "GGA" : "G", "GGG" : "G"
}

def main():
    with open("example.txt", "r") as f:
        rna_str = f.read()

    translated = ""
    for codon in range(0,len(rna_str), 3):
        sub = rna_str[codon: codon+3]        
        translated += codon_to_amino[sub]

    print(translated)

if __name__ == "__main__":
    main()