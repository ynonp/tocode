number = int(input("please choose a number"))
mod7 = int(number) % 7
for i in len(number):
    if number[i] == 7:
        cont7 = 1
    if mod7 == 0 or cont7 == 1:
        print("BOOM")
