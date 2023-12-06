def part1(lines: list[str]):

    def scoreLine(line: str) -> int:
        numbers = line.split(":")[1]
        winningNumbers, numbersYouHave = numbers.split("|")

        winningNumberSet = set()
        for num in winningNumbers.strip().split(" "):
            if num == "":
                continue
            winningNumberSet.add(int(num))

        total = 0
        for num in numbersYouHave.strip().split(" "):
            if num == "":
                continue
            total += int(num) in winningNumberSet

        return 2**(total - 1) if total else 0

    return sum(scoreLine(line) for line in lines)

def part2(lines: list[str]) -> int:

    prizes = {}

    def scoreLine(lineNum: int) -> list[int]:

        if lineNum in prizes:
            return prizes[lineNum]
        
        line = lines[lineNum - 1]
        numbers = line.split(":")[1]
        winningNumbers, numbersYouHave = numbers.split("|")

        winningNumberSet = set()
        for num in winningNumbers.strip().split(" "):
            if num == "":
                continue
            winningNumberSet.add(int(num))

        total = 0
        for num in numbersYouHave.strip().split(" "):
            if num == "":
                continue
            total += int(num) in winningNumberSet
        
        result = [i for i in range(lineNum + 1, lineNum + total + 1)]
        prizes[lineNum] = result
        return result
    
    cardCount = 0
    lineScores = {}
    for currentLine in reversed(range(1, len(lines) + 1)):
        cards = scoreLine(currentLine)
        print(cards)
        lineScores[currentLine] = sum(lineScores[card] for card in cards) if cards else 1
        cardCount += lineScores[currentLine]

    print(lineScores)
    return cardCount

def main():
    with open("sample.txt") as file:
        lines = [line.rstrip() for line in file.readlines()]
    
    res = part2(lines)
    print(res)

if __name__ == "__main__":
    main()