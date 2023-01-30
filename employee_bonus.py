import csv

with open("EmployeePay.csv", "r") as employeeFile:
    #Im using Dictreader to fetch row specific Data making this easier (essentially allowing me to pick a row based on its name in the first row)
    #Since the csv file you provided is setup in the proper way I can use DictReader. Essentially it treats the first line of the file as dictionary keys
    readFile = csv.DictReader(employeeFile)
   
    for row in readFile:
        #Establish all types of pay and Total Pay
        pay, bonus, totalpay = float(row["Salary"]), float(row["Bonus"]), (float(row["Salary"]) + (float(row["Bonus"])*float(row["Salary"])))

        print("Employee ID:", row["ï»¿ID"]) #For some reason the row is labeled as ï»¿ID So I used that as the row name to make it work, else i got a keyError
        #For reference if you'd like to find this, simply print(row). This prints the row name and shows the Ghost charachters so I can copy paste them
        print("Emp Name:", row["EmpFName"] + " " + row["EmpLName"])
        print("Salary:", "$" + str(pay))
        print("Bonus:", str(bonus*100)+"%")
        print("Total Pay:","$" + str(totalpay) + "\n")
    #I think I dont actually have to close my file but in C++ we did for memory leaks so I continue this habit here
    employeeFile.close()
       




