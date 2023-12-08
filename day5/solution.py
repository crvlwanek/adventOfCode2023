def part1():
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file.readlines()]

    seeds = [int(value) for value in lines[0].split(":")[1].split(" ") if value]

    maps = []
    for line in lines[2:]:
        if not line:
            continue

        if ":" in line:
            maps.append([])
            continue
        
        dest, source, length = line.split(" ")

        maps[-1].append({ 
            "low": int(source), 
            "high": int(source) + int(length), 
            "offset": int(dest) - int(source)
        })

    locations = []
    for seed in seeds:
        current = seed

        for mapType in maps:
            dest = None
            for key in mapType:

                if key["low"] <= current < key["high"]:
                    dest = current + key["offset"]
                    break

            current = dest or current

        locations.append(current)

    print(min(locations))

def part2():
    with open("sample.txt") as file:
        lines = [line.rstrip() for line in file.readlines()]

    seedRanges = []
    values = [int(value) for value in lines[0].split(":")[1].split(" ") if value]
    for seed, length in zip(values[::2], values[1::2]):
        seedRanges.append((seed, seed + length))

    maps = []
    for line in lines[2:]:
        if not line: continue

        if ":" in line:
            maps.append([])
            continue

        dest, source, length = [int(val) for val in line.split(" ")]
        maps[-1].append((source, source + length, dest - source))

    maps = [sorted(map) for map in maps]
    
    def searchMap(map, seedLow):
        for i, m in enumerate(map):
            mapLow, mapHigh, _ = m
            if mapLow <= seedLow < mapHigh:
                return i
            
        return -1


    for _map in maps:
        temp = []
        while seedRanges:
            seedLow, seedHigh = seedRanges.pop()
            index = searchMap(_map, seedLow)
            if index == -1:
                temp.append((seedLow, seedHigh))
                continue

            mapLow, mapHigh, offset = _map[index]

            if seedLow <= mapLow < seedHigh:
                temp.append((mapLow + offset, seedHigh + offset))
                seedRanges.append((seedLow, mapLow))
                continue

            if seedLow <= mapHigh < seedHigh:
                temp.append((seedLow + offset, mapHigh + offset))
                seedRanges.append((mapHigh, seedHigh))
                continue

            temp.append((seedLow + offset, seedHigh + offset))

        seedRanges = temp

    print(min(seedLow for seedLow, _ in seedRanges))





    

part2()