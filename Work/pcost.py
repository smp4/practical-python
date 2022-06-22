# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    '''
    Calculates the total cost of a portfolio from a file.
    '''

    total_cost = 0
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            try:
                nshares = int(row[1])
            except ValueError:
                print("Couldn't parse number of shares in line", row)
            try:
                price = float(row[2])
            except ValueError:
                print("Couldn't parse price in line", row)
            total_cost = total_cost + nshares * price

#    print(f"Total cost is ${total_cost:0.2f}")

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost:", cost)
