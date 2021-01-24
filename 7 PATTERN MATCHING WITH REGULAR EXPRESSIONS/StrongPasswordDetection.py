# Chapter 7
# Project: Strong Password Detection

# Regex that detects if password got:
# lenght of minimum 8 char
# Both upper and lowercases
# at least one digit

import re

# function that checks if password is strong*  
def CheckPassword(password):
    if len(password) >= 8:
        if re.compile(r'\d').search(password):
            if re.compile(r'[a-z]').search(password):
                if re.compile(r'[A-Z]').search(password):
                    return "This password is strong"
    return "This password is weak"


# Tests  

CheckPassword("aaaaaaaaaaa")
# return This password is weak
CheckPassword("1SCVr^mEp5FZq")
# return This password is strong
CheckPassword("AAAAaaaaa")
# return This password is weak
CheckPassword("AAAAaaaa78")
# return This password is strong
CheckPassword("aaa78aaaa")
# This password is weak
CheckPassword("password1")
# return This password is weak
CheckPassword("Password1")
# return This password is strong
