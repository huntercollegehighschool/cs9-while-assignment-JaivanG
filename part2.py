'''
***PART 2***

Write a program that prompts the user to enter a number. The program then prints "Hunter" the number of times the user entered. Use a while loop.

Example of what should appear when the program runs:

Times to print: 3
Hunter
Hunter
Hunter

'''
word=input("Enter a word: ")
printed=int(input("How many times do you want to print the word? "))
prints=1
while printed>= prints:
  prints=prints+1
  print(word)

if prints<printed:
  print("that's it")