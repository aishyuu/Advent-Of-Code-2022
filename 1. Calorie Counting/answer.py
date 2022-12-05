file = open("input.txt", "r")

elf_number = 1
elf_max = 0
current_calories = 0
max_calories = 0
all_elves = []

for line in file:
    if line == "\n":
        all_elves.append(current_calories)
        if current_calories > max_calories:
            max_calories = current_calories
            elf_max = elf_number
        current_calories = 0
        elf_number += 1
    else:
        current_calories += int(line)

print(f'Elf number {elf_number} has the most calories with {max_calories} calories')

all_elves.sort(reverse=True)
print(all_elves[0] + all_elves[1] + all_elves[2])