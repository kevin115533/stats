"""
File: stats.py

This programs finds the median, mode, and mean of a set of numbers
"""

def main():
    sum1 = 0.0
    count = 0
    number = input("Enter a number or press Enter to quit: ")
    while number != "":
        count += 1
        number = float(number)
        sum1 += number
        number = input("Enter a number or press Enter to quit: ")
    average = mean(sum1, count)
    print("The average number is", round(average,2))

def mean(x,y):
    return x / y


main()
