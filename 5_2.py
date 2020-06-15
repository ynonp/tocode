months = int(input("please enter your age in months:"))
# Again - I'd use a new variable. Also perhaps you'd want to format the value
age_in_years = months / 12

# So this format string limits the value to 2 digits after
# the floating point
print(f"your age in year is: {age_in_years:0.2f}")
