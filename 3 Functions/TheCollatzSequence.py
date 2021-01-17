# Chapter 3
# Project: the Collatz Sequence

def collatz(number):
    try:
        # If number is even
        if number % 2 == 0:
            return number // 2
        # if number is odd
        else:
            return 3 * number + 1
    # Error handling
    except ValueError:
        print("Number is noninteger")


print("Enter number:")
userNumber = int(input())

# Using this sequence, you’ll arrive at 1
while(True):
    userNumber = collatz(userNumber)
    print(userNumber)
    if(userNumber == 1):
        break
