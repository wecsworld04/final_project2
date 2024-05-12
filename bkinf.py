import csv

with open("bank_info.csv", mode='w') as csvfile:
    login_cred = ["first_name", "last_name", "pin_num", "checking", "savings"]
    writer = csv.DictWriter(csvfile, fieldnames=login_cred)
    writer.writeheader()
    writer.writerow({"first_name": "Emily", "last_name": "Smith", "pin_num": 1234, "checking": 100, "savings": 100})
    writer.writerow({"first_name": "Jacob", "last_name": "Johnson", "pin_num": 1234, "checking": 100, "savings": 100})
    writer.writerow({"first_name": "Mia", "last_name": "Brown", "pin_num": 1234, "checking": 100, "savings": 100})
    writer.writerow({"first_name": "Amelia", "last_name": "Williams", "pin_num": 1234, "checking": 100, "savings": 100})
    writer.writerow({"first_name": "Emily", "last_name": "Jones", "pin_num": 1234, "checking": 100, "savings": 100})
    writer.writerow({"first_name": "Charlotte", "last_name": "Davis", "pin_num": 1234, "checking": 100, "savings": 100})
    writer.writerow({"first_name": "Benjamin", "last_name": "Martinez", "pin_num": 1234, "checking": 100, "savings": 100})
    writer.writerow({"first_name": "Harper", "last_name": "Wilson", "pin_num": 1234, "checking": 100, "savings": 100})
    writer.writerow({"first_name": "Michael", "last_name": "Smith", "pin_num": 1234, "checking": 100, "savings": 100})
