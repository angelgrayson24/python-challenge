import csv

# Initialize variables to store data
months = []
profits_losses = []

# Read data from CSV
with open('resources/budget_data.csv') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        date = row[0]
        profit_loss = int(row[1])
        months.append(date)
        profits_losses.append(profit_loss)

# The total number of months included in the dataset
total_months = len(months)

# The net total amount of "Profit/Losses" over the entire period
net_total = sum(profits_losses)

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
changes = [profits_losses[i+1] - profits_losses[i] for i in range(len(profits_losses)-1)]
average_change = sum(changes) / len(changes)

# The greatest increase and decrease in profits (date and amount) over the entire period
greatest_increase = max(changes)
greatest_increase_date = months[changes.index(greatest_increase) + 1] 
greatest_decrease = min(changes)
greatest_decrease_date = months[changes.index(greatest_decrease) + 1]

# Print results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export results to a text file
output_path = "financial_analysis.txt"
with open(output_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("-----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Net Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

print(f"Results exported to {output_path}")