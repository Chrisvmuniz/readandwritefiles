import csv

#Since we want our code to be simpler, I am going to use a dictionary instead of a Array like we learnt in class. 
#This will make life easier especially when checking for existing customers vs adding new ones
dictionaryOfSales = {}

with open("sales.csv", "r") as salesFile:
    #Im using Dictreader to fetch row specific Data making this easier (essentially allowing me to pick a row based on its name in the first row)
    #Since the csv file you provided is setup in the proper way I can use DictReader. Essentially it treats the first line of the file as dictionary keys
    readFile = csv.DictReader(salesFile)
    for row in readFile:
        #Here I take the three row totals and add them to get a total Sales amount for the current row
        totalSaleAmount = float(row["SubTotal"]) + float(row["TaxAmt"]) + float(row["Freight"])
        
        #I then get the current Customers ID from the current row
        currentCustomer = row["ï»¿CustomerID"] #Again had to add the weird charachters in cause it has "Ghost" Charachters to avoid a key error
        #For reference if you'd like to find this, simply print(row). This prints the row name and shows the Ghost charachters so I can copy paste them
        
        #Then I check if this customer already exists in my sales dictionary based on keys
        if currentCustomer in dictionaryOfSales: #If it's the same customer (same key) keep adding to the total
            dictionaryOfSales[currentCustomer] += totalSaleAmount
        else: #If it's a different customer (key not in our dictionary) then make a new total and append it to the end of the dictionary
            dictionaryOfSales[currentCustomer] = totalSaleAmount
    #I think I dont actually have to close my file but in C++ we did for memory leaks so I continue this habit here
    salesFile.close()

#Fluff debugging line to make sure my dictionary was setup right As:
# {'250': 5255.24, '251': 26634.88, '252': 625.53, '253': 28735.62, '254': 43095.65, '255': 38747.020000000004, '256': 95202.76999999999, '257': 19802.719999999998, '258': 14795.87, '259': 32874.75, '260': 29710.260000000002, '261': 18098.01}
#print(dictionaryOfSales)

#Then we want to write in to our new file
with open("salesreport.csv", "w", newline="") as reportFile:
    #Here we setup the file writer from csv import to write into our file
    writeFile = csv.writer(reportFile)
    #Then we call .write row and label our rows
    writeFile.writerow(["Customer", "Total"])
    #We are iterating over the dictionary here (both key and what its tied to) so we have to use .items() to get everything
    for customer, total in dictionaryOfSales.items():
        #get the two and write them to my sales report row
        writeFile.writerow([customer, total])
    #I think I dont actually have to close my file but in C++ we did for memory leaks so I continue this habit here
    reportFile.close()
