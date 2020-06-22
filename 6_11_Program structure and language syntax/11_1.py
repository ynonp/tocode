# I think it's easier to solve this one
# without the list, look:

max_value = float('-inf')
for num in range(10):
    print(num + 1, " from 10")
    number = int(input("enter number\n"))
    max_value = max(max_value, num)
    # Or use if:
    # if number > max_value:
    #     max_value = number

print("the max num in list is: ", max_value)
