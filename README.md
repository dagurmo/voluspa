# voluspa
A small demonstration of Go for "Concurrent and Distributed Programming" at Reykjavik University.

J.R.R. Tolkien took inspiration from the Voluspa in naming the dwarves and Gandalf in The Hobbit.
Explore the effort it takes to test a concurrent program—the file voluspa.go at
https://github.com/mkyas/voluspa is a small program that starts a go routine for each name in the list
and prints it.

1. Read the code and explain how the program may be executed.
2. Develop a specification of this program's behaviour and write a method to verify that this program
   works as intended.
   1. You can write this program in any programming language that you are familiar with
   2. Your program should invoke the dwarves' program and read its output from standard input and
      output "yes" if valid and "no" otherwise.
