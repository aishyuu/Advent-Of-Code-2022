"""
So let's say cd gets popped into a stack
if we do "cd /", then we should add "/" to the stack
We also want to put it to a dictionary and add "/" with a value of 0
For everything that doesn't have the "$", we have to split and add numbers.
"""
import re

file = open("input.txt", "r")

directory_cache = []
directory_total = {}

def main():
    for line in file:
        if dollar_verify(line):
            command_caching(line)
        else:
            directory_sum(line)
    
    closest_to_hundredk()
    print(directory_total)

def dollar_verify(line):
    if re.findall(r"^\$", line):
        return True
    return False

def directory_sum(line):
    if line.startswith("dir "):
        return
    else:
        size = line.split(" ")
        for folder in directory_cache:
            directory_total[folder] += int(size[0])

def closest_to_hundredk():
    sum = 0
    for folder in directory_total:
        if directory_total[folder] > 100_000 or (sum + directory_total[folder] > 100_000):
            pass
        else:
            sum += directory_total[folder]
    
    print(sum)

def command_caching(line):
    if re.findall(r"\$ cd ", line):
        line_split = line.split(" ")
        line_split[2] = line_split[2][:len(line_split[2]) - 3]
        if line_split[2] == "":
            directory_cache.pop()
        else:
            directory_total[line_split[2]] = 0
            directory_cache.append(line_split[2])
        print(directory_cache)

if __name__ == "__main__":
    main()