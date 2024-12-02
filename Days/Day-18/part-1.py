
def parseInput():
    input = []

    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
        # some code for case-specific parsing
        
    return input


if __name__ == "__main__":
    input = parseInput()
