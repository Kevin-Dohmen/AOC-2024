def parseInput():
    left = []
    right = []

    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
        for line in input:
            split = line.split("   ")
            left.append(int(split[0]))
            right.append(int(split[1]))
    return left, right

def countNums(arr):
    numbers = []
    count = []
    for num in arr:
        if num not in numbers:
            numbers.append(num)
            count.append(1)
        else:
            count[numbers.index(num)] += 1
    return numbers, count

if __name__ == "__main__":
    left, right = parseInput()
    numbers, count = countNums(right)

    ssSum = 0
    for num in left:
        if num in numbers:
            ssSum += num * count[numbers.index(num)]
    
    print(ssSum)
