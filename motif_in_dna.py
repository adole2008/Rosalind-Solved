#Solution to Finding a Motif in DNA (link: https://rosalind.info/problems/subs/)


def main():
    with open("rosalind_subs.txt", "r") as f:
        string = f.readline().strip()
        sub = f.readline().strip()
        

    # string = "GATATATGCATATACTT"
    # sub = "ATAT"


    for i in range(0,(len(string)-len(sub))+1,1):
        cur = string[i:i+len(sub)]
        if cur == sub:
            print(f"{i+1} ", end="")

    
    print()


if __name__ == "__main__":
    main()