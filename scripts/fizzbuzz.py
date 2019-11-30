# Solution 1
# Concatenating Strings
for num in range(1,21):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)


# Solution 2
# Utilizing if, elif, and else

# an elif statement allows you to check multiple expressions
# for True and execute a block of code as soon as one of
# the conditions evaluates to True

for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
