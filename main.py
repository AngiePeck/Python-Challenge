#import os and csv

import os

import csv

with open("PyBank_data.csv", "r") as file_object:
    reader = csv.reader(file_object, delimiter = ",")
#print(contents)  #check that the reader works
    #Gets the total months
    next(reader) #skips the header
    month_count = 0
    months = list(reader)
    month_count = len(months)
print("Total Months: " + str(month_count))

with open("PyBank_data.csv", "r") as file_object:
    reader = csv.reader(file_object, delimiter = ",")
    next(reader) #skips the header
    total = 0 
    #Total of profit/losses
    for row in csv.reader(file_object):
        total += int(row[1])



with open("PyBank_data.csv", "r") as file_object:
    reader = csv.reader(file_object, delimiter = ",")
    next(reader) #skips the header
    is_first_row = 1
    last_value = 0
    diff_values = []
    current_value = 0
    for row in csv.reader(file_object):
        current_value = row[1]
        if is_first_row != 1:
            diff_values.append(int(current_value)-int(last_value))
        else:
            is_first_row = 0
        last_value = current_value
    #average calculation
    import statistics
    average = round(statistics.mean(diff_values),2)


with open("PyBank_data.csv", "r") as file_object:
    reader = csv.reader(file_object, delimiter = ",")
    next(reader) #skips the header
    greatest = 0
    lowest = 0
    for row in csv.reader(file_object):
        if int(row[1]) > greatest: 
            greatest = int(row[1])
            greatest_date = row[0]
        if int(row[1]) < lowest:
            lowest = int(row[1])
            lowest_date = row[0]
    highest  = 0
    smallest = 0
    for difference in diff_values:
       
        if int(difference) > highest: 
            highest = int(difference)
        
        if int(difference) < smallest:
            smallest = int(difference)

print("Total: " + "$" + str(total))
print("Average Change: $" + str(average))
print("Greatest Increase in Profits: " + str(greatest_date) + " " + "$" + str(highest))
print("Greatest Decrease in Profits: " + str(lowest_date) + " " + "$" + str(smallest))


output_file = open("bank_summary.txt", "w")
output_file.write("Total: " + "$" + str(total) + "\r\n")
output_file.write("Average Change: $" + str(average) + "\r\n")
output_file.write("Greatest Increase in Profits: " + str(greatest_date) + " " + "$" + str(highest) + "\r\n")
output_file.write("Greatest Decrease in Profits: " + str(lowest_date) + " " + "$" + str(smallest) + "\r\n") 
output_file.close()


