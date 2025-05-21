#Solution to Counting Point Mutations (link: https://rosalind.info/problems/hamm/)

#hamming distance: minimum number of point mutations needed to transform 1 string into another

def main():
    with open("rosalind_hamm.txt", "r") as f:
        seq1 = f.readline()
        seq2= f.readline()
    
    ct = sum([a != b for a,b in zip(seq1,seq2)])
    #zip() generates tuples, and saves memory (compared to original solution of using for loops)
    
    print(ct)

if __name__ == "__main__":
    main()