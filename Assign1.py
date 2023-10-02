# Name: Orayda Shagifa
# CS1026 Assignment 1: Inflation Rate
# Description: Program calculates personal inflation rate and type of inflation.
# Inflation rate = ((total expenses of current year - total expenses of the previous year)/(total expenses of the current year)) * 100%

totPYear = 0    # variable to store total expenses for the previous
totIntYear = 0  # variable to store total expenses for the current/interest year

curYear = int(input("Please enter the year that you want to calculate the personal interest rate for: "))   # stores year
numCat = int(input("Please enter the number of expenditure categories: "))  # stores number of expenditure categories

while numCat > 0:   # repeats for each expenditure category
    pYear = float(input("Please enter expenses for previous year: "))   # stores expenses for previous year
    intYear = float(input("Please enter expenses for year of interest: "))  # stores expenses for current year
    numCat = numCat - 1     # keeps track of number of times loop is repeated

    totPYear += pYear       # sums all previous year expenses
    totIntYear += intYear   # sums all current year expenses

infRate = (((totIntYear - totPYear) / totIntYear) * 100)    # inflation rate formula
print("Personal inflation rate for %d is %.1f%%" % (curYear, infRate))

# determines type of inflation based on inflation rate
if infRate < 3:
    print("Type of Inflation: Low")
elif 3 <= infRate < 5:
    print("Type of Inflation: Moderate")
elif 5 <= infRate < 10:
    print("Type of Inflation: High")
elif infRate >= 10:
    print("Type of Inflation: Hyper")
