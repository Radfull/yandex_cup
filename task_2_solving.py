
import math as m
from collections import Counter

def solve(path):
    with open(path, 'r') as f:
        n = int(f.readline())
        pairs = f.readlines()

    pairs = [i.rstrip() for i in pairs]
    pairs = [tuple(el for el in s.split())  for s in pairs]
    num_uniq_names = n+1
    uniq_names= set(i for s in pairs for i in s )
    count_names = Counter(i for s in pairs for i in s )

    num_rounds = m.log2(num_uniq_names)
    max_val =max(count_names.values())
    if len(uniq_names) == num_uniq_names and max_val == num_rounds:
        for i in pairs:
            if count_names[i[0]] == max_val  and count_names[i[1]] == max_val :
                return i[0] +' '+ i[1]
    return 'NO SOLUTION'

def main():
    print(solve('chess.txt'))

if __name__ == '__main__':
    main()