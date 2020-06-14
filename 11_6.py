a1 = int(input("Enter the first number of the invoice series: "))
d = int(input("Insert the difference between the organs in the series: "))
n = int(input("Insert the number of organs in the series: "))

sum_series = (n * ((2 * a1) + d * (n - 1))) / 2
print("sum of series is: ", sum_series)
