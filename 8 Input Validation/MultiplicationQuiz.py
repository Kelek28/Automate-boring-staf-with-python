# Chapter 8
# Project: Multiplication Quiz

import pyinputplus as pyip
import random

numberOfCorrectAnswers = 0
questionNumbers = 10
for i in range(questionNumbers):
    try:
        number1 = random.randint(0, 10)
        number2 = random.randint(0, 10)
        pyip.inputInt("Question number {}: {} x {} = ".format(i+1,
                                                              number1, number2),
                      allowRegexes=["^{}$".format(number1*number2)],
                      blockRegexes=[('.*', "Mistake")],
                      limit=3,
                      timeout=5)
    # if you make answer after 5 seconds
    except pyip.TimeoutException:
        print("You run out of time!")
    # if you make 3 mistakes
    except pyip.RetryLimitException:
        print("You run out of your tries")
    else:
        print("You get one point")
        numberOfCorrectAnswers += 1
# Score print
print('Score: {} of {}'.format(numberOfCorrectAnswers, i+1))
