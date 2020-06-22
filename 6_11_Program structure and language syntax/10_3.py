def read_number_stubbornly(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            print("Sorry - you typed something that wasn't a number. Try again")


x = read_number_stubbornly("Please select a first number: ")
y = read_number_stubbornly("Please select a second number: ")

print(f"{x} + {y} = {x + y}")
