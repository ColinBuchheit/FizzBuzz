#FizzBuzz Program
#Iterates from 1 to 100, printing "Fizz" for multiples of 3, "Buzz" for multiples of 5,
#and "FizzBuzz" for multiples of both 3 and 5. For all other numbers, it prints the number itself.

for i in range(1, 101):  #loop through numbers 1 to 100 (inclusive)
    output = ''  #initializes an empty string to hold the output for each number

    #checks for multiples of 3
    if i % 3 == 0:
        output += 'Fizz'  #checks the current number "i" of it is divisable by 3. If true it outputs Fizz

    #checks for multiples of 5
    if i % 5 == 0:
        output += 'Buzz'  #checks if the "i" os divisable by 5, if so, it outputs the Buzz

    #prints the output if not empty; otherwise, print the number itself
    print(output or i)
