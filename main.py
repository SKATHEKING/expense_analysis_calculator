# This application should be able to take input from user and based on this input generate a pdf based on spending

# importing modules
import csv
import datetime
import pandas as pd
from Tools.scripts.dutree import display
import matplotlib.pyplot as plt

#data structures for expenses
categories = ['Shopping', 'Withdrawals','Travel' ,'Leisure','Bills','Subscriptions','Transfers','Other']
expense = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
expenses_by_category = dict(zip(categories, str(expense)))
total_spent = 0.00

#makes sure that all expenses and bills are not empty and that the dictionary is populated
def ensure_not_empty():
    for category in categories:
        print(category)

    for spent in expense:
        print(spent)

    for key, val in expenses_by_category.items():
        print(key + ' ' + str(val))

#function that should run as main asking user questions about all their expenses
def expense_anotator():
    for key in expenses_by_category.keys():
        bill = float(input(f'How much have you spent in the following category? {key} \n'))
        expenses_by_category[key] = str(bill)

#Calculates total spent by person over period of time
def calculate_total_spent():
    total = 0.00
    for values in expenses_by_category.values():
        total += float(values)
    total_spent = total
    expenses_by_category['total'] = total
    print(total_spent)

#create CSV that can then further be analysed
def make_csv():
    with open('montlhy_spendings.csv', 'w') as f:
        w = csv.writer(f)
        w.writerow(expenses_by_category.keys())
        w.writerow(expenses_by_category.values())
#make graphs necessary for data visualization
def make_graphs():
    data = pd.read_csv('montlhy_spendings.csv')


    # Bar chart with day against tip
    plt.bar(data['categories'], data['expense'])

    plt.title("Monthly Spending")

    # Setting the X and Y labels
    plt.xlabel('Category')
    plt.ylabel('Money Spent')

    # Adding the legends
    plt.show()

#generate pdf
#runs all necessary functions to make all the program work
def main():
    ensure_not_empty()
    expense_anotator()
    calculate_total_spent()
    make_csv()
    make_graphs()

main()
