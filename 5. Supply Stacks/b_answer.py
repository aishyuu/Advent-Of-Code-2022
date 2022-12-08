import re

file = open("input.txt", "r")

def main():
    crate_lines = setup()
    final_lines = work(crate_lines)
    for line in final_lines:
        print(line[-1])

def work(crate_lines):
    #Starting from the line that starts with "move _ from _ to _"
    for line in file:
        #Find all the numbers only in that line
        move, take_from, put_to = re.findall(r" \d+", line)
        #Change them to int
        move, take_from, put_to = int(move), int(take_from), int(put_to)

        crate_cache = []

        for _ in range(0, move):
            #Take from the row you want to take from and put it in the row you want to add to
            crate_cache.append(crate_lines[take_from-1].pop())

        crate_cache.reverse()

        for thing in crate_cache:
            crate_lines[put_to-1].append(thing)

    
    return crate_lines

def setup():
    """
    Set up the lists and put them in proper order for however many crate lines there are

    :return: crate_lines
    :return type: List
    """
    first = False

    #Since the file is sorted in a specific way, we adjust to that order
    for line in file:
        #For the first line, we set up the 2d matrix needed to adjust for all the crates
        if not first:
            crate_lines = [[] for _ in line[1::4]]
            first = True

        #If there is a line break, then that means the problem begins and we can stop here
        if line == "\n":
            print("Break")
            break

        #We take all the letters in the current line into a list
        current_line = line[1::4]
        line_index = 0

        #Add the letter to their respective crate line (row in the 2d matrix)
        for letter in current_line:
            if letter == " ":
                line_index += 1
                continue
            crate_lines[line_index].append(current_line[line_index])
            line_index += 1
    
    #We take out the last value which are the numbers
    for line in range(0, len(crate_lines)):
        crate_lines[line].pop()
        #Reverse the list to make it a stack instead of a queue
        crate_lines[line].reverse()

    return crate_lines


if __name__ == "__main__":
    main()