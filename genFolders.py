import os

pythonTemplate = """
def parseInput():
    input = []

    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
        # some code for case-specific parsing
        
    return input


if __name__ == "__main__":
    input = parseInput()
"""

def createFolder(i):
    name = f"Day-{i}"
    if not os.path.exists(name):
        os.makedirs(name)
    
    with open(name + "/README.md", "w") as f:
        f.write(f"# [**Advent of Code 2024 - Day {i}**](https://adventofcode.com/2024/day/{i})\n\n## Description\n")
    
    with open(name + "/input.txt", "w") as f:
        f.write("")
    
    with open(name + "/example.txt", "w") as f:
        f.write("")
    
    with open(name + "/part-1.py", "w") as f:
        f.write(pythonTemplate)

    with open(name + "/part-2.py", "w") as f:
        f.write(pythonTemplate)
    


if __name__ == "__main__":
    if not os.path.exists("Days"):
        os.makedirs("Days")
    os.chdir("Days")
    for i in range(1, 26):
        createFolder(i)
