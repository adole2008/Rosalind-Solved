#Solution to Mendel's First Law (link: https://rosalind.info/problems/iprb/ )

def count_dominants(A, B, C):
    return 4*(choose_pair(A)) + 4*(A*B) + 4* (A*C) + 3 *(choose_pair(B)) + 2*(B*C)

def factorial(n):
    if n==1 or n<=0:
        return 1
    return n*factorial(n-1)


def choose_pair(n):
    return int(factorial(n)/(factorial(2) * factorial(n-2)))


def main():

    with open("rosalind_iprb.txt", "r") as f:
        text = f.read()
        list = text.split(" ")
        dominant = int(list[0])
        heterozygous = int(list[1])
        recessive = int(list[2])

    favorable = count_dominants(dominant, heterozygous, recessive)

    orgs = dominant + heterozygous + recessive
    all_possible = int((factorial(orgs)/(factorial(2) * factorial(orgs-2)))*4)

    print(favorable/all_possible)


if __name__ == "__main__":
    main()