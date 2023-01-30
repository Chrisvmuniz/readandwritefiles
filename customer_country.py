import csv

with open("customers.csv", "r") as customerInputFile, open("customer_country.csv", "w", newline="") as outputFile:
    #Im using Dictreader to fetch row specific Data making this easier (essentially allowing me to pick a row based on its name in the first row)
    #Since the csv file you provided is setup in the proper way I can use DictReader. Essentially it treats the first line of the file as dictionary keys
    readFile = csv.DictReader(customerInputFile)
    #Then I open up writer for my writing out
    writer = csv.writer(outputFile)

    #Then we write the titles of our rows to the new files, in this case we want the Customers name (Full customer name) and Country as the two row headers
    writer.writerow(["Customer Name", "Country"])

    #then we simply iterate throught readFiles rows and get the rows we want through the keys, then write them (in write row form) 
    #as a joint first and last name and the country seperated by a comma to seperate rows
    for row in readFile:
        #Note I could not solve special charachters like accents on the charachters
        #print(str(row["FirstName"] + " " + row["LastName"])) #I was trying to fix it but just couldnt figure out how
        #I recognise it has to do with 'utf-8' but could not figure out how to fix this sorry
        writer.writerow([str(row["FirstName"] + " " + row["LastName"]), row["Country"]])

    #I think I dont actually have to close my file but in C++ we did for memory leaks so I continue this habit here
    customerInputFile.close()
    outputFile.close()