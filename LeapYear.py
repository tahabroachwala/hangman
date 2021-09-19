# Any year evenly divisible by 4 is a leap year

def isLeapYear(year, divisor):
    return year % divisor == 0
i = 2021
year_list = []
while i < 2042:
    if isLeapYear(i, 4):
        if isLeapYear(i, 100):
            if isLeapYear(i, 400):
                year_list.append(i)
        else:
            year_list.append(i)       
    i += 1
for i in year_list:
    print(i)




