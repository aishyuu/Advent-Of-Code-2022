"""
So let's say cd gets popped into a stack
if we do "cd /", then we should add "/" to the stack
We also want to put it to a dictionary and add "/" with a value of 0
For everything that doesn't have the "$", we have to split and add numbers.
"""
import re

file = open("example_input.txt", "r")

directory_cache = []
directory_sum = {}

def main():
    for line in file:
        if dollar_verify(line):
            command_caching(line)
        else:
            print("non command")
    
    print(directory_sum)

def dollar_verify(line):
    if re.findall(r"^\$", line):
        return True
    return False

def command_caching(line):
    if re.findall(r"\$ cd ", line):
        line_split = line.split(" ")
        line_split[2] = line_split[2][:len(line_split[2]) - 3]
        if line_split[2] == "":
            directory_cache.pop()
        else:
            directory_sum[line_split[2]] = 0
            directory_cache.append(line_split[2])
        print(directory_cache)
    else:
        print("Not valid command")

if __name__ == "__main__":
    main()