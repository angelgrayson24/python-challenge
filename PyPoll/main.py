import csv

# Initialize variables
total_votes = 0
candidate_votes = {}

# Read data from CSV
with open('Resources/election_data.csv') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# The total number of votes cast
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# The percentage of votes each candidate won/ and The total number of votes each candidate won
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

# The winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export results to a text file
output_path = "election_results.txt"
with open(output_path, "w") as output_file:
    output_file.write

print(f"Results exported to {output_path}")