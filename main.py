"""Alex Vigil"""
# This program will showcase my understanding of the Python coding language

name = input("Enter your name: ")
# stores whatever the user inputs to the variable name

print("Hello ", name, " my name is Alex Vigil and welcome to the showcase "
                      "of my Python knowledge", sep='', end='.')
# outputs statement with the variable added to it, the sep= operator makes
# the variable integrate to the strings in a smoother fashion, and the end=
# operator adds a period to the end of the string literal

print('')
# empty string used for spacing

print("Firstly we will be learning about numeric operators and how they "
      "function.")
print("These operators include: ")
print('')
print('+', '-', '*', '/', '**', '//', '%', sep='\n')
print('')
# This section of code lists all the available numeric operators on their
# own individual line, the empty print statements are for formatting

condition = 0
# This is the condition for the while loop that will make it run
# continuously unless broken

while condition == 0:
    # This is a while loop that will run the block of code written within it
    # until the condition is broken

    print("If you want to stop learning about numeric operators please "
          "enter 1.")
    nOperator = input("Enter the numeric operator you would like to learn"
                      " about: ")
    # whatever is inputted for this variable will determine what
    # information is output from the IF statements

    print('')
    # empty string used for spacing

    if nOperator == '+':
        # the if statement makes it so that the block of code under it will
        # only run if the IF condition is met
        print("The + symbol represents addition and adds two values "
              "together")
        print('1 + 1 =', 1 + 1)
        print('')
        # This section shows how the addition works in python

    elif nOperator == '-':
        print("The - symbol represents subtraction and subtracts two "
              "values together")
        print('2 - 1 =', 2 - 1)
        # This line represents a subtraction equation and the use of -
        print('')

    elif nOperator == '*':
        print("The * symbol represents multiplication and multiplies two "
              "values together")
        print('2 * 2 =', 2 * 2)
        print('')
        # This section shows how multiplication works in python

    elif nOperator == '/':
        print("The / symbol represents division and divides two values "
              "together")
        print('4 / 2 =', 4 / 2)
        print('')
        # This section shows how division works in python

    elif nOperator == '**':
        print("The ** symbol represents an exponent and will multiply the "
              "base number by itself x amount of times decided by the "
              "second value inputted")
        print('2 ** 3 =', 2 ** 3)
        print('')
        # This section shows how exponents work in python

    elif nOperator == '//':
        print("The // symbol represents floor division and will divide "
              "both numbers inputted and output the highest amount of "
              "times the second input can go into the first input")
        print('5 // 2 =', 5 // 2)
        print('')
        # This section hows floor division works in python

    elif nOperator == '%':
        print("The % symbol represents modulus and it will divide the "
              "first input by the second and output the remainder")
        print('5 % 2 =', 5 % 2)
        print('')
        # This section of code explains the modulus operator in python

    elif nOperator == '1':
        condition += 1
        print('')
        # This section will break the while loop if the number one is inputted

    else:
        print("Wrong value inputted please try again")
        print('')
        # This section covers user error and will prompt the user to reenter a
        # value to match the ones provided

print("Next I will demonstrate my knowledge of string operators.")
print("The two string operators I am gonna cover are the + and * "
      "operators.")
print("These symbols are similar to the symbols used for addition and "
      "multiplication but they behave differently when used on string "
      "literals.")
# description of string operators and which ones will be covered
print('')

condition2 = 0
# The condition that keeps the while loop running

while condition2 == 0:
    # while loop that will run the block of code inside of it until the
    # condition is broken

    print("If you want to stop learning about string operators please "
          "enter 1.")
    # if 1 is entered the condition of the while loop will be broken
    sOperator = input("Enter the string operator you would like to "
                      "learn about: ")
    print('')
    # asks the user to input a number for the if statement

    if sOperator == '+':
        print("The + operator concatenates two strings together meaning that "
              "it combines two separate strings into one string literal.")
        print("Hello", '+', "World", "= HelloWorld")
        print('')
    # This section covers the concatenation operators and how it combines
    # strings together.

    elif sOperator == '*':
        print("The * operator will output a string however many times you "
              "repeat it which is decided by the integer value you put next "
              "to the operator.")
        print("Hello World * 3 = Hello World Hello World Hello World")
        print('')
    # This section shows how multiplication symbol works on strings and shows
    # the output produced my multiplying a string

    elif sOperator == '1':
        condition2 += 1
    # If the elif condition is met then the while loop is broken

    else:
        print("Wrong value inputted please try again.")
        print('')
    # If the value inputted does not meet any of the conditions then you will
    # try again

print('')
print("Next we will be covering relational operators. They compare the "
      "operands inputted on either side of the operator and return a True or "
      "False value depending if the appropriate conditions are met.")
print("These operators include: ")
print('')
print('==', '!=', '>', '>=', '<', '<=', sep='\n')
print('')
# shows that relational operators will be covered next
# the \n is to ensure that every string literal is printed on an individual
# line

condition3 = 0
# The condition for the while loop

while condition3 == 0:
    # while loop that will run the block of code inside of it until the
    # condition is broken

    print("If you want to stop learning about relational operators please "
          "enter 1.")

    rOperator = input("Enter the relational operator you would like to learn "
                      "about: ")
    # asks user to enter number for the if statement
    print('')

    if rOperator == '==':
        print("The == operator is the equal to sign and will return a True "
              "value if the operands are equal to each other and a False "
              "value if they are not.")
        print("1 == 1 = True")
        print("1 == 2 = False")
        print('')
        # this block of code covers the equal sign operator

    elif rOperator == '!=':
        print("The != operator is the not equal to sign and will return a "
              "True value if the operands are not equal to each other and a "
              "False value if they are.")
        print("1 != 1 = False")
        print("1 != 2 = True")
        print('')
        # this block of code covers the not equal to sign operator

    elif rOperator == '>':
        print("The > operator is the greater than sign and will return a True "
              "value if the first operand is greater than the second. It will "
              "return a False value if the first operand is less than the "
              "second.")
        print("1 > 0 = True")
        print("1 > 1 = False")
        print("1 > 2 = False")
        print('')
        # this block of code covers the greater than operator

    elif rOperator == '>=':
        print("The >= operator is the greater than or equal to sign and will "
              "return a True value if the first operand is greater or equal "
              "to the second. It will return a False value if the first "
              "operand is less than or not equal to the second.")
        print("1 >= 0 = True")
        print("1 >= 1 = True")
        print("1 >= 2 = False")
        print('')
        # this block of code covers the greater than or equal to operator

    elif rOperator == '<':
        print("The < operator is the less than sign and will return a True "
              "value if the first operand is less than the second. It will "
              "return a False value if the first operand is greater than the "
              "second operand.")
        print("1 < 0 = False")
        print("1 < 1 = False")
        print("1 < 2 = True")
        print('')
        # this block of code covers the less than operator

    elif rOperator == '<=':
        print("The <= operator is the less than or equal to sign and will "
              "return a True value if the first operand is less than or equal "
              "to the second. It will return a False value if the first "
              "operand is greater than or not equal to the second.")
        print("1 <= 0 = False")
        print("1 <= 1 = True")
        print("1 <= 2 = True")
        print('')
        # this block of code covers the less than or equal to operator

    elif rOperator == '1':
        condition3 += 1
        # this block of code covers what to input to break the while loop

    else:
        print("Wrong value inputted please try again.")
        print('')
        # this covers user error for the while loop

print("Lastly I will be covering Boolean operators, they are used to compare "
      "values and control the flow of a program. The three boolean operators "
      "are: ")
print('')
print("not", "and", "or", sep='\n')
print('')
# this block of code covers the final peace of the project which is boolean
# operators and then lists off each one on their respective line.

condition4 = 0
# condition for the while loop

while condition4 == 0:
    # while loop that will run the block of code inside of it until the
    # condition is broken

    print("If you want to stop learning about boolean operators please"
          "enter 1.")
    # tells the user how to break the loop
    bOperator = input("Enter the boolean operator you would like to learn "
                      "about: ")
    print('')
    # asks the user to input number to learn about boolean operators

    if bOperator == 'not':
        print("The not operator inverts the value of your boolean expression.")
        print("a = True")
        print("b = not a")
        print("b = False")
        print('')
        # this block of code covers the not operator

    elif bOperator == 'and':
        print("The and operator combines the values of boolean expressions to "
              "help control the flow of the program.")
        print("a = True")
        print("b = False")
        print("c = True")
        print("a and b = False")
        print("a and c = True")
        print('')
        # this block of code covers the and operator

    elif bOperator == 'or':
        print("The or operator returns a True value if either one or both of "
              "the operands.")
        print("are True")
        print("a = True")
        print("b = False")
        print("c = True")
        print("d = False")
        print("a or b = True")
        print("a or c = True")
        print("b or d = False")
        print('')
        # this block of code covers the or operator

    elif bOperator == '1':
        condition4 += 1
        # this block of code covers how to break the loop

    else:
        print("Wrong value inputted please try again.")
        print('')
        # this block of code covers user error for the input

print("That will be all for today, thank you", name, "for letting me show you "
      "the basics of the python language.")

# This section is the ending statement and it includes the variable within the
# string to make the ending seem more personal to the viewer
