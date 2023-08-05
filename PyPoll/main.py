import pandas as pd


df = pd.read_csv("Resources/election_data.csv")

# The total number of votes cast
total_votes = len(df)

#  complete list of candidates who received votes
candidates = df["Candidate"].unique()

# The percentage of votes each candidate won
candidate_votes = df["Candidate"].value_counts()
percent_votes = (candidate_votes / total_votes) * 100

# The total number of votes each candidate won
total_votes_per_candidate = candidate_votes

# The winner of the election based on popular vote
winner = candidate_votes.idxmax()

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {percent_votes[candidate]:.3f}% ({total_votes_per_candidate[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# Export the results to a text file
with open("election_results.txt", "w") as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")
    for candidate in candidates:
        f.write(f"{candidate}: {percent_votes[candidate]:.3f}% ({total_votes_per_candidate[candidate]})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")