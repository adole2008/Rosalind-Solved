#Solution for Calculating Expected Offspring (link: https://rosalind.info/problems/iev/)

# plug into expected value formula, every couple has exactly 2 offspring

def main():
    with open("rosalind_iev.txt", "r") as f:
        str = f.read().strip()
        arr = list(map(int, str.split(" ")))

    print(calc_expected_value(arr))

def calc_expected_value(arr):
    return arr[0] * 2.0 + arr[1] * 2.0 + arr[2] * 2.0 + arr[3] * 0.75 * 2.0 + arr[4]

if __name__ == "__main__":
    main()