import numpy as np
import csv

with open("C:\\Users\\DELL\\Downloads\\py.csv", 'r')as file:
    csv_file = csv.DictReader(file)
    fname = []
    lname = []

    for row in csv_file:
        dict_converter = dict(row)
        print(dict_converter)
        f = dict_converter["fname"]
        l = dict_converter["lname"]
        fname.append(f)
        lname.append(l)

domain = "@amazon.com"
fname_total = len(fname)
print(fname_total)
fname_total_variable = fname_total
if fname_total == fname_total_variable:
    print("Fname count is:", fname_total_variable)
else:
    print("Error")

lname_total = len(lname)
print(lname_total)
lname_total_variable = lname_total
if lname_total == lname_total_variable:
    print("Lname count is:", lname_total_variable)
else:
    print("Error")

mapping_dot = list(map(lambda x,y: x+'.'+y, fname,lname))
print(mapping_dot)
email = []
for i in mapping_dot:
    print(i)
    email_creation = i+domain
    print(email_creation)
    p = len(email_creation)
    if p <= 52:
        print("Length is perfect")
    else:
        print("Not Perfect")
    email.append(email_creation)
    print(email)
    count_email = len(email)
    print(count_email)

    if fname_total == lname_total == count_email:
        print("Count of source and target is perfect")
    else:
        print("Not Perfect")
