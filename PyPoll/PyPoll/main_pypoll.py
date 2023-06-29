import os
import csv
csv_path=os.path.join("Resources","election_data.csv")

with open(csv_path,newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
    list_cndt = [cndt[2] for cndt in csv_reader]
    
total_votes = len(list_cndt)

cndt_info = [[cndt,list_cndt.count(cndt)] for cndt in set(list_cndt)]
 
cndt_info = sorted(cndt_info, key=lambda x: x[1], reverse=True)

print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")

for cndt in cndt_info:
    percent_votes = (cndt[1] / total_votes) * 100
    print(f"{cndt[0]}: {percent_votes:6.3f}% ({cndt[1]})")

print("---------------------------")
print(f"Winner: {cndt_info[0][0]}")
print("---------------------------")

output_file = os.path.join("Resources", "PyPoll_Results.txt")
with open(output_file, "w") as txt_file:
    print("Election Results", file=txt_file)
    print(f"Total Votes: {total_votes}", file=txt_file)

    for cndt in cndt_info:
        percent_votes = (cndt[1] / total_votes) * 100
        print(f"{cndt[0]}: {percent_votes:6.3f}% ({cndt[1]})", file=txt_file)
    print(f"Winner: {cndt_info[0][0]}", file=txt_file)