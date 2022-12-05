file = open("input.txt", "r")

def main():
    total = 0
    current_three = []
    current_loop = 1
    for line in file:
        if current_loop < 3:
            current_three.append(line[:-1])
            current_loop += 1
        else:
            current_three.append(line[:-1])
            a=list(set(current_three[0])&set(current_three[1])&set(current_three[2]))
            total += number_value(a[0])
            current_loop = 1
            current_three = []
    
    print(total)

def number_value(common):
    ascii_value = int(ord(common))
    if common[0].islower():
            return ascii_value - 96
    else:
        return ascii_value - 38

def find_common(s):
    first, second = s[:len(s)//2], s[len(s)//2:]
    a=list(set(first)&set(second))
    return a[0]

if __name__ == "__main__":
    main()