with open("input.txt") as file:
    lines = [line.rstrip() for line in file.readlines()]

times, distances = [[string for string in line.split(" ") if string and string.isdigit()] for line in lines]
print(times)
print(distances)