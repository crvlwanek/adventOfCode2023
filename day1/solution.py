def part1(lines: list[str]) -> int:
    total = 0
    for line in lines:
        indicies = [i for i, val in enumerate(line) if val.isdigit()]
        leftIndex, rightIndex = indicies[0], indicies[-1]
        total += int(line[leftIndex]) * 10 + int(line[rightIndex])

    return total

def part2(lines: list[str]) -> int:

    def getWordFromIndex(line: str, index: int) -> int:

        wordPrefixes = {
            "on": "one", "tw": "two", "th": "three",
            "fo": "four", "fi": "five", "si": "six",
            "se": "seven", "ei": "eight", "ni": "nine"
        }

        word = wordPrefixes[line[index:index+2]]
        return numberWords[word]
    
    total = 0
    for lineIndex, line in enumerate(lines, start=1):

        indicies = [i for i, val in enumerate(line) if val.isdigit()]
        leftIndex, rightIndex = indicies[0], indicies[-1]

        numberWords = {
            "one": 1, "two": 2, "three": 3,
            "four": 4, "five": 5, "six": 6,
            "seven": 7, "eight": 8, "nine": 9
        }

        wordIndiciesLeft = [line.find(word) for word in numberWords.keys()]
        wordIndiciesLeft = [index for index in wordIndiciesLeft if index != -1]

        wordIndiciesRight = [line.rfind(word) for word in numberWords.keys()]
        wordIndiciesRight = [index for index in wordIndiciesRight if index != -1]


        minWordIndex = min(wordIndiciesLeft) if len(wordIndiciesLeft) > 0 else float("inf")
        maxWordIndex = max(wordIndiciesRight) if len(wordIndiciesRight) > 0 else -1

        if leftIndex < minWordIndex:
            leftDigit = int(line[leftIndex])
        else:
            leftDigit = getWordFromIndex(line, minWordIndex)
        
        if rightIndex > maxWordIndex:
            rightDigit = int(line[rightIndex])
        else:
            rightDigit = getWordFromIndex(line, maxWordIndex)
        
        total += leftDigit * 10 + rightDigit

    return total


def main():
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file.readlines()]

    return part2(lines) 


if __name__ == "__main__":
    result = main()
    print(result)