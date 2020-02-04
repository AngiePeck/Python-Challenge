#import os and csv

import os

import csv

with open("PyBank_data.csv", "r") as file_object:
    reader = csv.reader(file_object, delimiter = ",")
#print(contents)  #check that the reader works
    #Get the total months
    next(reader)
    month_count = 0
    months = list(reader)
    month_count = len(months)
print("Total Months: " + str(month_count))

with open("PyBank_data.csv", "r") as file_object:
    reader = csv.reader(file_object, delimiter = ",")
    next(reader)
    total = 0 
    greatest = 0
    lowest = 0
    #Total profit/losses
    for row in csv.reader(file_object):
        total += int(row[1])
        if int(row[1]) > greatest: 
            greatest = int(row[1])
            greatest_date = row[0]
        if int(row[1]) < lowest:
            lowest = int(row[1])
            lowest_date = row[0]

print("Total: " + str(total))

print("Average Change: " + str(total/month_count))

print("Greatest Increase in Profits: " + str(greatest_date) + " " + str(greatest))

print("Greatest Decrease in Profits: " + str(lowest_date) + " " + str(lowest))





