import re
from collections import defaultdict

data = open("input.txt").read().strip()
lines = [x for x in data.split('\n')]

totals = defaultdict(int)
cache = []

def main():

    for line in lines:
        words = line.strip().split()
        if words[1] == "cd":
            if words[2] == "..":
                cache.pop()
            else:
                cache.append(words[2])
        elif words[1] == "ls":
            continue
        else:
            try:
                sz = int(words[0])
                # print(cache)
                for i in range(len(cache) + 1):
                    totals["/".join(cache[:i])] += sz
            except:
                pass
    
    max_used = 70000000 - 30000000
    total_used = totals['/']
    need_to_free = total_used - max_used

    best = 1e9
    ans = 0

    for k, v in totals.items():
        if v >= need_to_free:
            best = min(best, v)
            print(k, v)
        
        if v <= 100_000:
            ans += v
    
    print(ans)
    print(best)

if __name__ == "__main__":
    main()