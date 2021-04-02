import os
import csv

csvfilepath = os.path.join("Resources", "PyPoll_Resources_election_data.csv")

votes = 0
candidates = []
candidateVote = []
candidatePercent = []

with open(csvfilepath, newline='', encoding='utf-8') as handler:
	csvreader = csv.reader(handler, delimiter=',')

	csvheader = next(csvreader)

	for row in csvreader:
		votes = votes + 1
		if row[2] not in candidates:
			candidates.append(row[2])
			candidateVote.append(1)
		else:
			candidateVote[candidates.index(row[2])] += 1

for i in candidateVote:
	candidatePercent.append(round(100*i/votes, 3))

outpath = os.path.join("Analysis", "election_analysis.txt")

with open(outpath, 'w', newline='', encoding='utf-8') as file:
	csvwriter = csv.writer(file)

	csvwriter.writerow(["Election Results"])
	csvwriter.writerow(["-------------------------------------"])
	csvwriter.writerow([f"Total Votes: {votes}"])
	csvwriter.writerow(["-------------------------------------"])
	for j in range(len(candidates)):
		csvwriter.writerow([f"{candidates[j]}: {candidatePercent[j]}% ({candidateVote[j]})"])
	csvwriter.writerow(["-------------------------------------"])
	csvwriter.writerow(["Winner: " + candidates[candidateVote.index(max(candidateVote))]])
	csvwriter.writerow(["-------------------------------------"])

print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {votes}")
print("-------------------------------------")
for m in range(len(candidates)):
	print(f"{candidates[m]}: {candidatePercent[m]}% ({candidateVote[m]})")
print("-------------------------------------")
print("Winner: " + candidates[candidateVote.index(max(candidateVote))])
print("-------------------------------------")