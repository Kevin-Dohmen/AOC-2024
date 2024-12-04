
def parseInput():
    input = []

    with open('input.txt', 'r') as file:
        tmp = file.read().splitlines()
        input = [[*x] for x in tmp]
        
    return input

def check (input: list[list[str]], x: int, y: int) -> int:
    count = 0
    for xd in range(-1, 2):
        for yd in range(-1, 2):
            if xd == 0 and yd == 0:
                continue
            xd1, yd1 = x, y
            xd2, yd2 = x + xd, y + yd
            xd3, yd3 = x + xd * 2, y + yd * 2
            xd4, yd4 = x + xd * 3, y + yd * 3
            if 0 <= xd4 < len(input[0]) and 0 <= yd4 < len(input):
                string = "".join([input[yd1][xd1], input[yd2][xd2], input[yd3][xd3], input[yd4][xd4]])
                if string == "XMAS":
                    count += 1
    return count

if __name__ == "__main__":
    input = parseInput()
    count = 0
    for y in range(len(input)):
        for x in range(len(input[0])):
            count += check(input, x, y)
    print(count)
