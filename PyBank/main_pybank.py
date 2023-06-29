import os
import csv
csv_path=os.path.join("Resources","budget_data.csv")

budget_data=[]
with open(csv_path) as csvfile:
    csv_reader=csv.DictReader(csvfile)

    for row in csv_reader:
        budget_data.append({"month":row["Date"],"amount":int(row["Profit/Losses"]),"change":0})

total_months=len(budget_data)

previous_amount=budget_data[0]["amount"]
for i in range(total_months):
    budget_data[i]["change"] = budget_data[i]["amount"] - previous_amount
    previous_amount=budget_data[i]["amount"]

total_amount=sum(row["amount"] for row in budget_data)
total_amount_change=sum(row["change"] for row in budget_data)
average=round(total_amount_change/(total_months-1),2)
greatest_increase=max(budget_data, key=lambda x:x["change"])
greatest_decrease=min(budget_data, key=lambda x:x["change"])

print("Financial Analysis")
print(f"Total Months:{total_months}")
print(f"Total:${total_amount}")
print(f"Average Change:${average}")
print(f"Greatest Increase in Profits:{greatest_increase['month']} (${greatest_increase['change']})")
print(f"Greatest Decrease in Profits:{greatest_decrease['month']}(${greatest_decrease['change']})")

Exportfile = os.path.join("Resources", "PyBank_Results.txt")
with open(Exportfile, "w") as txtfile:
    print("Financial Analysis", file=txtfile)
    print(f"Total Months: {total_months}", file=txtfile)
    print(f"Total: ${total_amount}", file=txtfile)
    print(f"Average Change: ${average}", file=txtfile)
    print(f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['change']})", file=txtfile)
    print(f"Greatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['change']})", file=txtfile)

