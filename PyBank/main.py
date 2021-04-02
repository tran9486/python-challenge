import os
import csv

csvfilepath = os.path.join("Resources", "budget_data.csv")

monthCount = 0
netProfit = 0.0
incMax = 0.0
incDate = ''
decMax = 0.0
decDate = ''

with open(csvfilepath, newline='', encoding='utf-8') as handler:
	csvreader = csv.reader(handler, delimiter=',')

	csvheader = next(csvreader)

	for row in csvreader:
		monthCount = monthCount + 1
		netProfit = netProfit + float(row[1])
		if float(row[1]) > incMax:
			incMax = float(row[1])
			incDate = row[0]
		if float(row[1]) < decMax:
			decMax = float(row[1])
			decDate	= row[0]

outpath = os.path.join("Analysis", "budget_analysis.txt")

with open(outpath, 'w', newline='', encoding='utf-8') as file:
	csvwriter = csv.writer(file)

	csvwriter.writerow(["Financial Analysis"])
	csvwriter.writerow(["------------------------------------"])
	csvwriter.writerow(["Total Months: " + str(monthCount)])
	csvwriter.writerow(["Total: $" + str(netProfit)])
	csvwriter.writerow(["Average Change: $ " + str(netProfit/monthCount)])
	csvwriter.writerow([f"Greatest Increase in Profits: {incDate} ({incMax})"])
	csvwriter.writerow([f"Greatest Decrease in Profits: {decDate} ({decMax})"])

print("Financial Analysis")
print("------------------------------------")
print("Total Months: " + str(monthCount))
print("Total: $" + str(netProfit))
print("Average Change: $" + str(netProfit/monthCount))
print(f"Greatest Increase in Profits: {incDate} ({incMax})")
print(f"Greatest Decrease in Profits: {decDate} ({decMax})")