file = open("example.txt", "r")

def main():
    total_points = 0
    for line in file:
        opponent, you = line.split()
        opponent = translate_opponent(opponent)
        total_points += full_points(opponent, you)
    
    print(total_points)

def full_points(opponent, you):
    match you:
        case 'X':
            match opponent:
                case 'X':
                    return choice_point('Z') + victory_point(opponent, 'Z')
                case 'Y':
                    return choice_point('X') + victory_point(opponent, 'X')
                case 'Z':
                    return choice_point('Y') + victory_point(opponent, 'Y')
        case 'Y':
            match opponent:
                case 'X':
                    return choice_point('X') + victory_point(opponent, 'X')
                case 'Y':
                    return choice_point('Y') + victory_point(opponent, 'Y')
                case 'Z':
                    return choice_point('Z') + victory_point(opponent, 'Z')
        case 'Z':
            match opponent:
                case 'X':
                    return choice_point('Y') + victory_point(opponent, 'Y')
                case 'Y':
                    return choice_point('Z') + victory_point(opponent, 'Z')
                case 'Z':
                    return choice_point('X') + victory_point(opponent, 'X')
    ...

def choice_point(you):
    match you:
        case 'X':
            return 1
        case 'Y':
            return 2
        case 'Z':
            return 3

def translate_opponent(choice):
    match choice:
        case 'A':
            return 'X'
        case 'B':
            return 'Y'
        case 'C':
            return 'Z'

def victory_point(opponent, you):
    if opponent == you:
        return 3
    if (you == 'X' and opponent == 'Z') or (you == 'Y' and opponent == 'X') or (you == 'Z' and opponent == 'Y'):
        return 6
    else: 
        return 0

if __name__ == "__main__":
    main()