## Voluspa
A small demonstration of Go for "Concurrent and Distributed Programming" at Reykjavik University.

J.R.R. Tolkien took inspiration from the Völuspá in naming the dwarves and Gandalf in The Hobbit.
Explore the effort it takes to test a concurrent program—the file voluspa.go at
https://github.com/mkyas/voluspa is a small program that starts a go routine for each name in the list
and prints it.

# How to run a Go file

Use the command "go run voluspa.go" to run the voluspa.go file

# How to run test-voluspa.py for verification

Since the test file is written in the python language you can simply press "play" in your enviornment or use the command below.

"python test-voluspa.py" or "python3 test-voluspa.py"

# Specification 

The test program should verify the following 
- Correct format of output lines
- Correct number of dwarfs
- Correct dwarf names
