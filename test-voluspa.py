import subprocess
import re


def verification_of_voluspa():
    dwarves = {
        "Þorinn", 
        "Balin", 
        "Bífurr", 
        "Báfurr", 
        "Bömburr", 
        "Dóri", 
        "Dvalinn", 
        "Fíli", 
        "Glóinn", 
        "Kíli", 
        "Nóri", 
        "Þrainn", 
        "Óri", 
        "Gandalfr"
    }

    try:
        result = subprocess.run(["go", "run", "voluspa.go"], capture_output=True, text=True, encoding="utf-8")
    except FileNotFoundError:
        print("no")
        return
    
    # Get the last word in each line representing the dwarves
    output = result.stdout.strip().split("\n")

    check_format(output)

    # Get the names of dwarfs from the output
    for i in range(len(output)):
        output[i] = output[i].split()[-1]

    check_length(output)

    check_names(output, dwarves)
    
    print("yes")


def check_format(output):
    
    # Check format of the output ("Hi! My name is", name)
    pattern = r"^Hi! My name is (.+)$"
    names = set()
    for line in output:
        match = re.match(pattern, line)
        if not match:
            print("no")
            exit(1)
        names.add(match.group(1))

def check_length(output):

    if len(output) != 14: # Check if the output has the correct number of names
        print("no")
        exit(1)

def check_names(output, dwarves):
    for line in output:
        if line not in dwarves:
            print("no")
            exit(1)

if __name__ == '__main__':
    verification_of_voluspa()