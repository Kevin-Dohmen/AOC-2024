import re

def parseInput():
    input = []

    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
        # some code for case-specific parsing
        
    return input

if __name__ == "__main__":
    input = parseInput()
    regex = r"don't\(\)|do\(\)|mul\([0-9]*,[0-9]*\)"

    opSum = 0

    do = True

    for line in input:
        for op in re.findall(regex, line):
            opOutput = 0
            print(op)
            if op[:3] == "mul" and do:
                a, b = op[4:-1].split(",")
                opOutput = int(a) * int(b)
                print(opOutput)
            elif op == "do()":
                do = True
            elif op == "don't()":
                do = False
            opSum += opOutput
    
    print(opSum)
            
                
