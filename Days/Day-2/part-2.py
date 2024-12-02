def parseInput():
    input = []

    with open('input.txt', 'r') as file:
        tmp = file.read().splitlines()
        tmp2 = [i.split(' ') for i in tmp]
        for item in tmp2:
            input.append([int(i) for i in item])
        
    return input

if __name__ == "__main__":
    input = parseInput()
    
    safeCount = 0
    for item in input:
        safeSolutions = 0
        for i in range(len(item)):
            tmpItem = [item[x] for x in range(len(item)) if x != i]
            print(tmpItem)
            increasing = tmpItem[1] > tmpItem[0]
            tmpSafe = True

            for j in range(len(tmpItem) - 1):
                diff = tmpItem[j + 1] - tmpItem[j]
                oopsie = False
                if increasing and diff <= 0:
                    oopsie = True

                if not increasing and diff >= 0:
                    oopsie = True

                if 0 < abs(diff) > 3:
                    oopsie = True
                
                if oopsie:
                    tmpSafe = False
                    break
            if tmpSafe:
                safeSolutions += 1
        print(input.index(item) + 1, safeSolutions)
        if safeSolutions >= 1:
            safeCount += 1
    
    print(safeCount)
