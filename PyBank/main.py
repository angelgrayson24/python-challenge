import pandas as pd

df = pd.read_csv("Resources/budget_data.csv")

# The total number of months included in the dataset
total_months = len(df)

# The net total amount of "Profit/Losses" over the entire period
net_total = df["Profit/Losses"].sum()

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
df["Change"] = df["Profit/Losses"].diff()

average_change = df["Change"].mean()

#The greatest increase in profits (date and amount) over the entire period
max_increase = df[df["Change"] == df["Change"].max()]
max_increase_date = max_increase["Date"].values[0]
max_increase_amount = max_increase["Change"].values[0]

# The greatest decrease in profits (date and amount) over the entire period
max_decrease = df[df["Change"] == df["Change"].min()]
max_decrease_date = max_decrease["Date"].values[0]
max_decrease_amount = max_decrease["Change"].values[0]

# print analysis to terminal
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase_amount})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease_amount})")