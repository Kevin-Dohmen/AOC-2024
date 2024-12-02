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
    
    safe = 0
    for item in input:
        tmpSafe = True
        increasing = item[1] >= item[0]
        for i in range(len(item) - 1):
            diff = item[i + 1] - item[i]
            
            if increasing and diff <= 0:
                tmpSafe = False
                break

            if not increasing and diff >= 0:
                tmpSafe = False
                break

            if 0 < abs(diff) > 3:
                tmpSafe = False
                break
        if tmpSafe:
            safe += 1
    
    print(safe)
