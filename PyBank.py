import os
import csv

csvpath = os.path.join('budget_data.csv')

net_change = []
total_pl = []
greatest_increase = 0
greatest_decrease = 0
increase_date_range = ""
decrease_date_range = ""


with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csv_reader)

    #handle first month
    first_row = next(csv_reader)
    previous_month = float(first_row[1])
    total_months = 1
    total_pl.append(float(first_row[1]))

    for row in csv_reader:
        total_months += 1
        profit_loss = float(row[1])
        
        #Calculate net change
        current_net_change = profit_loss - previous_month
        previous_month = float(row[1])
        net_change.append(current_net_change)
        total_pl.append(profit_loss)

        #Greatest increase in profit
        if current_net_change > greatest_increase: 
            greatest_increase = current_net_change
            increase_date_range = row[0]

        #Greatest decrease in profit
        if current_net_change < greatest_decrease:
            greatest_decrease = current_net_change
            decrease_date_range = row[0]


    total_sum = sum(total_pl)
    average = sum(net_change)/len(net_change)
    print(total_months)
    print(total_sum)
    print(greatest_decrease)
    print(greatest_increase)
    print(average)

    #Summary
    Summary = (
        f"Financial Analysis\n"

        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_sum}\n"
        f"Average  Change: ${average:.2f}\n"
        f"Greatest Increase in Profits: {increase_date_range} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {decrease_date_range} (${greatest_decrease})\n")

    # Create text file
    with open("summary.txt", "w") as txt:
        txt.write(Summary)
    
