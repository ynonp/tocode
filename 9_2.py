def sum_digits(n):
    result = 0
    while n > 0:
        digit = n % 10
        print(digit)
        result += digit
        n //= 10
        print(n)

    print(f"Sum of digits is {result}")


num = int(input("Enter number: "))
sum_digits(num)
