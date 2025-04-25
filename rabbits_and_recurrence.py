# Solution to rabbits_and_recurrence (link: https://rosalind.info/problems/fib/ )

def fib(num_iter, pairs):
    if num_iter == 0:
        return 0
    if num_iter == 1:
        return 1
    return fib(num_iter-1,pairs) + pairs*fib(num_iter-2,pairs)

def main():
    with open( "rosalind_fib.txt", 'r') as f:
        list = []
        li = f.read()

       # print(li)
        list = li.split(" ")
        #print(list)
        
        
    print(fib(int(list[0]),int(list[1])))

if __name__ == "__main__":
    main()