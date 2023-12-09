from collections import Counter

with open("input.txt") as file:
    lines = [line.rstrip() for line in file.readlines()]

def part1():
    key = {
        "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14
    }

    def score(card: str) -> int:
        if card.isdigit():
            return int(card)
        
        return key[card]

    def getHandType(counterCounts):
        if counterCounts[5]:
            return 7 # Five of a kind
        if counterCounts[4]:
            return 6 # Four of a kind
        if counterCounts[3] and counterCounts[2]:
            return 5
        if counterCounts[3]:
            return 4
        if counterCounts[2] == 2:
            return 3
        if counterCounts[2]:
            return 2
        return 1

    def scoreHand(hand: str):
        cards = hand.split(" ")[0]
        counter = Counter(cards)
        counterCounts = Counter(counter.values())
        handScore = (getHandType(counterCounts), 
            (score(cards[0]), score(cards[1]), score(cards[2]), score(cards[3]), score(cards[4]))
        )

        return handScore    


    lines.sort(key=scoreHand)
    winnings = 0
    for i, line in enumerate(lines, start=1):
        bid = int(line.split(" ")[1])
        winnings += i * bid

    print(winnings)


def part2():
    key = {
        "T": 10, "J": 1, "Q": 12, "K": 13, "A": 14
    }

    def score(card: str) -> int:
        if card.isdigit():
            return int(card)
        
        return key[card]
    
    def getHandType(counter, counterCounts):
        jokerCount = counter["J"]
        counter["J"] = 0
        maxOtherCard = max(counter.values())
        if counterCounts[5] or jokerCount + maxOtherCard == 5:
            return 7
        if counterCounts[4] or jokerCount + maxOtherCard == 4:
            return 6
        # Full house
        if (
            (counterCounts[3] and counterCounts[2]) or
            (counterCounts[3] and jokerCount > 0) or
            (counterCounts[2] == 2 and jokerCount > 0)
        ):
            return 5
        # 3 of a kind
        if counterCounts[3] or jokerCount + maxOtherCard == 3:
            return 4
        # 2 pair
        if (counterCounts[2] == 2) or (counterCounts[2] and jokerCount > 0):
            return 3
        # 1 pair
        if counterCounts[2] or jokerCount > 0:
            return 2

        return 1

    def scoreHand(hand: str):

        cards = hand.split(" ")[0]
        counter = Counter(cards)
        counterCounts = Counter(counter.values())
        handScore = (
            getHandType(counter, counterCounts),
            (score(cards[0]), score(cards[1]), score(cards[2]), score(cards[3]), score(cards[4]))
        )
        return handScore
    
    lines.sort(key=scoreHand)
    winnings = 0
    for i, line in enumerate(lines, start=1):
        bid = int(line.split(" ")[1])
        winnings += bid * i

    print(winnings)

part2()