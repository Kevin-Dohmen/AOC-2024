import os

def createFolder(name):
    if not os.path.exists(name):
        os.makedirs(name)
        with open(name + "/description.md", "w") as f:
            f.write(f"# {name}\n\n## Description\n")

if __name__ == "__main__":
    createFolder("Days")
    os.chdir("Days")
    for folder in [f"Day-{i}" for i in range(1, 26)]:
        createFolder(folder)
