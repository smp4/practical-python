# mortgage.py
#
# Exercise 1.7
#
# Exercise 1.9:
#   Total paid 878389.99
#   Number of months 309

principle = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment_start_month = 5*12 + 1
extra_payment_end_month = extra_payment_start_month + 4 * 12
extra_payment = 1000

while principle > 0:
    months = months + 1

    if extra_payment_start_month <= months and extra_payment_end_month >= months:
        total_payment = payment + extra_payment
    else:
        total_payment = payment

    principle = principle * (1 + rate / 12) - total_payment
    total_paid = total_paid + total_payment

    if principle < 0:
        total_payment =  principle + total_payment
        principle = 0
        print("Last payment is reduced. Only pay", round(total_payment,2))

    print(round(months, 2), round(total_paid, 2), round(principle, 2))

# print("Total paid", round(total_paid, 2))
##  print("Number of months", months)
