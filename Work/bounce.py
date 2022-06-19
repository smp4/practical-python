# bounce.py
#
# Exercise 1.5
bounce_height = 100 # metres
bounces = 0

while bounces < 10:
    bounces = bounces + 1
    bounce_height = bounce_height * 3 / 5
    print(bounces, round(bounce_height, 4))

