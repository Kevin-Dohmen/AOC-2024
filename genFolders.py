import os

def createFolder(i):
    name = f"Day-{i}"
    if not os.path.exists(name):
        os.makedirs(name)
    
    with open(name + "/README.md", "w") as f:
        f.write(f"# [**Advent of Code 2024 - Day {i}**](https://adventofcode.com/2024/day/{i})\n\n## Description\n")

if __name__ == "__main__":
    os.makedirs("Days")
    os.chdir("Days")
    for i in range(1, 26):
        createFolder(i)
