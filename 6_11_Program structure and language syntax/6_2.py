num = int(input("Please select a number: "))

if num % 2 == 0:
    print("The number is even")
elif num % 3 == 0:
    print("The number is divisable by 3")
elif num % 5 == 0:
    print("The number is divisable by 5")
else:
    print("The number is not divisable by 2,3 or 5")

print("--- The end ---")
