with open("input.txt") as file:
    lines = [line.rstrip() for line in file.readlines()]

def part1():
    
    def scoreLine(line):

        history = [[int(val) for val in line.split(" ")]]

        while not all(not val for val in history[-1]):
            history.append([history[-1][i+1] - val for i, val in enumerate(history[-1][:-1])])

        return sum(h[-1] for h in history)
    
    print(sum(scoreLine(line) for line in lines))

part1()