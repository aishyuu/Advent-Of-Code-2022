"""
Given 2 pairs of sections (6-6,4-6)
Implement code that checks if one group completely overlaps the other
"""

file = open("input.txt", "r")

def main():
    print(overlap(file))


def overlap(file):
    #Keep a tally of how many schedules overlap
    elf_overlap = 0
    for line in file:
        #Split the elf sections into two by splitting into two through ","
        elf_one, elf_two = line.split(",")

        #Continue splitting it into two through "-"
        elf_one = elf_one.split("-")
        elf_two = elf_two.split("-")

        #Make a list of ranges for both elf sections (+1 on end for inclusivity)
        section_one = [*range(int(elf_one[0]), int(elf_one[1]) + 1, 1)]
        section_two = [*range(int(elf_two[0]), int(elf_two[1]) + 1, 1)]

        #Check if all of one elf's sections is in the other elf's sections and vice versa
        check = all(item in section_one for item in section_two)
        check2 = all(item in section_two for item in section_one)

        #If sections completely overlap, add 1 to elf_overlap tally
        if check or check2:
            elf_overlap += 1

    #Return result
    return elf_overlap


if __name__ == "__main__":
    main()