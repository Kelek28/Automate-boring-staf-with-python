# Chapter 7
# Project: Date Detection

# regular expression that can detect dates in the DD/MM/YYYY format
import re
# Regex that check date in format DD/MM/YYYY
# DD in range 01-31
# MM in range 01-12
# YYYY in range 1000 - 2999
dateRegex = re.compile(
    r'(([1-2]\d|[0][1-9]|[3][0-1])\/([0][1-9]|[1][0-2])\/([1]\d\d\d|[2]\d\d\d))')

# check if date is in format DD/MM/YYYY


def CheckDateRegex(date):
    mo = dateRegex.search(date)
    if mo:
        result = "Date match DD/MM/YYYY format"
        if IsDateValid(mo.group(1)):
            return result + " and date is valid"
        return result + " but is not valid"
    return "Date don't match DD/MM/YYYY format"

# Function detects is year is leap


def IsLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        return False
    return True

# Check if date is Valid


def IsDateValid(date):
    monthAndDays = {
        '01': 31,
        '02': 28,
        '03': 31,
        '04': 30,
        '05': 31,
        '06': 30,
        '07': 31,
        '08': 31,
        '09': 30,
        '10': 31,
        '11': 30,
        '12': 31,

    }
    date = date.split('/')
    day = int(date[0])
    month = date[1]
    year = int(date[2])
    # check if february
    if month == "02":
        if IsLeapYear(year) and day <= 29:
            return True
    if monthAndDays[month] >= day:
        return True
    return False


# Date match DD/MM/YYYY format and date is Valid
print(CheckDateRegex("13/07/1954"))
# Date match DD/MM/YYYY format but is not valid
print(CheckDateRegex("29/02/1900"))
# Date don't match DD/MM/YYYY format
print(CheckDateRegex("13/07/3000"))
# Date match DD/MM/YYYY format but is not valid
print(CheckDateRegex("29/02/2008"))
# Date match DD/MM/YYYY format and date is Valid
print(CheckDateRegex("31/01/1543"))
