# Chapter 7
# Project: Regex Version of the strip() Method

import re
# If no other arguments are passed other than the string to strip,
# then whitespace characters will be removed from the beginning and end of the string.
# Otherwise, the characters specified in the second argument to the function will be removed from the string.


def RegexStrip(string, char=""):
    if not char:
        regex = re.compile(r'^\s+|\s+$')
    else:
        regex = re.compile(
            r'(?:^[{character}]+)|[{character}]+|(?:[{character}]+$)'.format(character=re.escape(char)))
    result = regex.sub("", string)
    return result


# return Hello World
RegexStrip("           Hello World              ")

# return Hello World
RegexStrip("///////Hello World///////", '/')

# return            Heo Word
RegexStrip("           Hello World              ", "l")

# return            Hello World
RegexStrip("           Hello World!              ", "!")

# return ello World
RegexStrip("Hello World", "H")
