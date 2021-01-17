# Chapter 4
# Project: Comma Code

def separateWithCommaAnd(list):
    answer = ""
    lenghtOfList = len(list)
    for word in list:
        if(list.index(word) == lenghtOfList - 1):
            answer = answer[:-2]
            answer += " and " + str(word)
            break
        answer += str(word)+", "
    return answer


# should return
# apples, bananas, tofu and cats
spam = ['apples', 'bananas', 'tofu', 'cats']
print(separateWithCommaAnd(spam))

# should return
# 1, 3, 5 and 7
spam1 = [1, 3, 5, 7]
print(separateWithCommaAnd(spam1))

# should return
# cat, 9, hello and 12
spam2 = ['cat', 9, "hello", 12]
print(separateWithCommaAnd(spam2))


# output
# apples, bananas, tofu and cats
# 1, 3, 5 and 7
# cat, 9, hello and 12
