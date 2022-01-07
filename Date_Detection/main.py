#Date Detection
import re

def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False

def isValidDate(date):
    day = date[0:2]
    month = date[3:5]
    year = date[6:10]
    if int(year) > 1000 and int(year) < 2999:
        if isLeapYear(int(year)):
            if int(month) in [1,3,5,7,8,10,12] and int(day) in range(1,32):
                return True
            elif int(month) in [4,6,9,11] and int(day) in range(1,31):
                return True
            elif int(month) == 2 and int(day) in range(1,30):
                return True
        else:
            if int(month) in [1,3,5,7,8,10,12] and int(day) in range(1,32):
                return True
            elif int(month) in [4,6,9,11] and int(day) in range(1,31):
                return True
            elif int(month) == 2 and int(day) in range(1,29):
                return True
    return False



def dateExtract(str):
    dateRegex = re.compile(r'\d{2}/\d{2}/\d{4}')
    dateList = dateRegex.findall(str)
    return dateList

sampleString = """Write a regular expression that can detect dates in the DD/MM/YYYY format.
Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999.
Note that if the day or month is a single digit, it\’ll have a leading zero.
The regular expression doesn\’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021.
Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date.
April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years.
Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400.
Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.
Example of valid dates are 07/01/2021, 01/01/2000, and 31/12/1999.
"""
listDate = dateExtract(sampleString)

for date in listDate:
    if isValidDate(date):
        print(date  + ": Valid date")
    else:
        print(date  + ": Invalid date")