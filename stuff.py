import csv

"""
The User Data. Save data and add new accounts
"""
def data(csV):
    # write data to csv file
    with open(csV, "w") as f:
        writer = csv.writer(f)
        writer.writerows(["user, password"])

    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)