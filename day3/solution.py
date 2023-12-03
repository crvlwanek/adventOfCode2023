import functools

def part1(lines: list[str]) -> int:

    lines = [[char for char in line] for line in lines]

    def isSymbol(char: str) -> bool:
        return not char.isdigit() and not char == "."
    
    rows, cols = len(lines), len(lines[0])

    def inBounds(x: int, y: int) -> bool:
        return 0 <= y < rows and 0 <= x < cols

    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]

    total = 0

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if not isSymbol(char):
                continue

            for dx, dy in directions:
                x2, y2 = x + dx, y + dy
                if not inBounds(x2, y2) or not lines[y2][x2].isdigit():
                    continue

                digits = []
                while inBounds(x2, y2) and lines[y2][x2].isdigit():
                    x2 -= 1

                x2 += not lines[y2][x2].isdigit() or not inBounds(x2, y2)

                while inBounds(x2, y2) and lines[y2][x2].isdigit():
                    digits.append(lines[y2][x2])
                    lines[y2][x2] = "."
                    x2 += 1

                total += int("".join(digits))

    return total

def part2(lines: list[str]) -> int:

    rows, cols = len(lines), len(lines[0])

    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]

    def inBounds(x: int, y: int) -> bool:
        return 0 <= x < rows and 0 <= y < cols
    
    def charIsDigit(x: int, y: int) -> bool:
        return inBounds(x, y) and lines[y][x].isdigit()
    
    def extractNumber(x: int, y: int) -> str:
        if not lines[y][x].isdigit():
            return ""
        
        digits = []

        while charIsDigit(x, y):
            x -= 1

        x += not lines[y][x].isdigit() or not inBounds(x, y)

        while charIsDigit(x, y):
            digits.append(str(x) + ":" + str(y))
            x += 1

        return ";".join(digits)

    def intFromHash(num: str) -> int:
        digits = []
        indicies = num.split(";")
        for index in indicies:
            sx, sy = index.split(":")
            digits.append(lines[int(sy)][int(sx)])

        return int("".join(digits))

    total = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if not char == "*":
                continue

            numSet = set()
            for dx, dy in directions:
                x2, y2 = x + dx, y + dy
                num = extractNumber(x2, y2)
                if num:
                    numSet.add(num)

            if len(numSet) != 2:
                continue
            
            nums = [intFromHash(num) for num in numSet]
            total += functools.reduce(lambda x, y: x * y, nums, 1)
    
    return total


def main():
    
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file.readlines()]
    
    result = part2(lines)
    print(result)

if __name__ == "__main__":
    main()