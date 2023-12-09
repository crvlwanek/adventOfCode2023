with open("input.txt") as file:
    lines = [line.rstrip() for line in file.readlines()]

def part1(lines):
    times, distances = [[int(string) for string in line.split(" ") if string and string.isdigit()] for line in lines]

    total = 1
    for time, distance in zip(times, distances):
        race = [i * (time - i) for i in range(time + 1)]
        total *= sum(True for r in race if r > distance)

    print(total)

def part2BruteForce(lines):
    time = int("".join(char for char in lines[0] if char.isdigit()))
    distance = int("".join(char for char in lines[1] if char.isdigit()))

    race = [i * (time - i) for i in range(time + 1)]
    print(sum(True for r in race if r > distance))

part2BruteForce(lines)