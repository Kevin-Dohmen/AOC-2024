
def parseInput():
    input = []

    with open('input.txt', 'r') as file:
        tmp = file.read().splitlines()
        input = [[*x] for x in tmp]
        
    return input

def check (input: list[list[str]], x: int, y: int) -> bool:
    tlx, tly = x - 1, y - 1
    trx, try_ = x + 1, y - 1
    blx, bly = x - 1, y + 1
    brx, bry = x + 1, y + 1
    if input[y][x] == "A":
        if input[tly][tlx] == "M" and input[bry][brx] == "S" or input[tly][tlx] == "S" and input[bry][brx] == "M":
            if input[bly][blx] == "M" and input[try_][trx] == "S" or input[bly][blx] == "S" and input[try_][trx] == "M":
                return True
    return False

if __name__ == "__main__":
    input = parseInput()
    count = 0
    for y in range(1, len(input) - 1):
        for x in range(1, len(input[0]) - 1):
            count += 1 if check(input, x, y) else 0
    print(count)
