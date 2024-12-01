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

def sort(arr: list):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == "__main__":
    left, right = parseInput()
    left = sort(left)
    right = sort(right)

    # print(left)
    # print(right)

    sumDist = 0
    for i in range(len(left)):
        sumDist += left[i] - right[i] if left[i] > right[i] else right[i] - left[i]
    print(sumDist)
