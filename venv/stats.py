"""
File: stats.py

This programs finds the median, mode, and mean of a set of numbers
"""
import statistics

def main():
    count = 0
    number = input("Enter a number or press Enter to quit: ")
    numberList = []
    while number != "":
        count += 1
        number = float(number)
        numberList = numberList + [number]
        number = input("Enter a number or press Enter to quit: ")
    average = mean(numberList, count)
    print("The average number is", round(average,2))
    print("The median number is", round(median(numberList),2))
    print("The mode of list of numbers is ", mode(numberList))

def mean(x,y):
    return sum(x) / y

def median(x):
    return statistics.median(x)

def mode(x):
    return statistics.mode(x)

main()
