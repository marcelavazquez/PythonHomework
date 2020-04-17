#Dependencies
import os
import csv

#Looking for the csv file
csvpath= os.path.join('Resources', 'budget_data.csv')

#Open and reading the CSV file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    #Create empty lists to store data
    months = []
    totalAmount = []
    
    #iterate through the rows
    for row in csvreader:
        months.append(row[0])
        totalAmount.append(int(row[1]))
    
    change = []
    
    #DUDAAAAS
    #len se refiere a la ultima posicion que tiene el array totalAmount
    for i in range(1,len(totalAmount)):
        change.append((int(totalAmount[i]) - int(totalAmount[i-1])))
    
    #La suma de la todos los datos de la operacion que hizo append entre el numero de datos que hay
    avgChange = sum(change)/len(change)

    # Obtain max and min value from the change list done before
    greatIncrease = max(change)
    greatDecrease = min(change)

    # Correlate the values with their months and index from max and min
    #We use the plus 1 at the end since month associated with change is the + 1 month or next month
    greatIncreaseMonth = change.index(max(change))+1
    greatDecreaseMonth = change.index(min(change))+1

    print(f"Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total: ${str(sum(totalAmount))}")
    print(f"Average Change: ${str(round(avgChange))}")
    print(f"Greatest Increase in Profits: {months[greatIncreaseMonth]} (${(str(greatIncrease))})")
    print(f"Greatest Decrease in Profits: {months[greatDecreaseMonth]} (${(str(greatDecrease))})")

    # Export to txt file
    txtfile = open("txtfile.txt", "w")

    line1 = "Financial Analysis"
    line2 = "---------------------"
    line3 = str(f"Total Months: {len(months)}")
    line4 = str(f"Total: ${str(sum(totalAmount))}")
    line5 = str(f"Average Change: ${str(round(avgChange))}")
    line6 = str(f"Greatest Increase in Profits: {months[greatIncreaseMonth]} (${(str(greatIncrease))})")
    line7 = str(f"Greatest Decrease in Profits: {months[greatDecreaseMonth]} (${(str(greatDecrease))})")
    txtfile.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))