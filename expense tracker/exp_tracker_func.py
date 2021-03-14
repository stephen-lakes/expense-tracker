from datetime import datetime
from tabulate import tabulate
import json

filename = "db.json"

def choices():
    instruction = f'''
    Choose "1" to add an expenditure
    Choose "2" to view recent expenditures
    Choose "3" to edit data(detailed view)
    Choose "4" to clear all data
    Choose "5" to close the app
    '''
    print(instruction)

def view_expenses():
    rows = []
    with open(filename, mode="r") as f:
        temp = json.load(f)
        for item in temp:
            row = (item["expenditure"], item["cost"], item["date"])
            rows.append(row)
    print(tabulate(rows, headers=["Expenditure", "Cost", "Date"]))
                       
def add():
    new_data = {}
    new_data["expenditure"] = input("Expenditure > ").strip().capitalize()
    new_data["cost"] = eval(input("Cost > "))
    exp_date = datetime.now()
    new_data["date"] = str(exp_date.day) + str(exp_date.month) + str(exp_date.year)
    new_data["date"] = f'{exp_date.day}/{exp_date.month}/{exp_date.year}'
    with open(filename, mode="r") as f:
        temp = json.load(f) # temp is a list object
    temp.append(new_data)

    with open(filename, mode="w") as f:
        json.dump(temp, f, indent=4, ensure_ascii=False)

def clear():
    with open(filename, mode="r") as f:
        temp = json.load(f)
    temp.clear()
    with open(filename, mode="w") as f:
        json.dump(temp, f, ensure_ascii=False)
        