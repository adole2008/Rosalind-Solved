#Solution for mortal fibonacci rabbits (link: https://rosalind.info/problems/fibd/)
#gng idk how to solve ts


def main():
    with open("example.txt", "r") as f:
        l = f.read().strip().split(" ")
        n = int(l[0])
        m = int(l[1])
    
    print(n,m)
    print(fib_original(n))
    print(fib(n))

def fib(n):
    if n == -1:
        return 0
    if n==0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-3)

def fib_original(n):
    if n==0:
        return 0 
    if n==1:
        return 1
    return fib_original(n-1) + fib_original(n-2)


if __name__ == "__main__":
    main()