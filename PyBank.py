import os
import csv

csvpath = os.path.join(r'C:\Users\sethl\Downloads\Python\python1\budget_data.csv')

net_change = []

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csv_reader)

    total_months = 0

    for row in csv_reader:
        total_months += 1
        profit_loss = int(row[1])
        net_change.append(profit_loss)
    total_sum = sum(net_change)
    print(total_months)
    print(total_sum)

# TODO: Create Variables to Keep Track of outcome


Total_Months = 0
Net_Change_List = []
Greatest_Increase = 0
Greatest_Decrease = 0
Total_Net_Change = 0

with open(csvpath) as csvfile:

    # CSV reader specifies delimieter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # TODO Read header row
    csv_header = next(csvreader)
    #print(f'CSV Header: {csv_header}')

    
    # TODO Use for loop to read through the file (hint look for "for row... in netflix activity")

    
    

        # TODO Track total month and total net change
        #lines= len(list(csvreader))
    
    
        

        # TODO Calculate current netchange and previous net change


        # TODO Add net_change to a list


        # TODO Logic to identify greatest net change increase


        # TODO Logic to identify greatest net change decrease


# TODO Calculate the Average Net Change
    

# TODO Generate Output Summary


# TODO Write result to txt file


    