def part1(games: list[str]) -> int:

    maxCubes = {
        "red": 12, "green": 13, "blue": 14
    }

    def getGameId(game: str) -> int:
        return int(game.split(":")[0].split(" ")[1])

    def isGameGood(game: str) -> bool:
        seen = { "red": 0, "green": 0, "blue": 0 }
        cubeSets: str = game.split(":")[1]
        for cubeSet in cubeSets.split(";"):
            for singleColor in cubeSet.split(","):
                singleColor = singleColor.strip()
                value, color = singleColor.split(" ")
                seen[color] = max(seen[color], int(value))

        return all(seen[color] <= maxCubes[color] for color in seen.keys())
    
    return sum(getGameId(game) for game in games if isGameGood(game))

def part2(games: list[str]) -> int:

    def findPower(game: str):
        seen = { "red": 0, "blue": 0, "green": 0 }
        cubeSets = game.split(":")[1]
        for cubeSet in cubeSets.split(";"):
            for singleColor in cubeSet.split(","):
                singleColor = singleColor.strip()
                value, color = singleColor.split(" ")

                seen[color] = max(seen[color], int(value))

        return seen["red"] * seen["blue"] * seen["green"]
    
    return sum(findPower(game) for game in games)


def main():
    with open("input.txt") as file:
        games = [line.rstrip() for line in file.readlines()]

    return part2(games)

if __name__ == "__main__":
    result = main()
    print(result)