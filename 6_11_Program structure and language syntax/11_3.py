list = []


def read_lines(prompt):
    while True:
        row = (input(prompt))
        if not row.strip():
            break
        else:
            list.append(row)
            print(list)

# A reminder - in class we saw how to solve this without a list
text = ''
while True:
    next_line = input()
    if len(next_line) == 0: break
    text = next_line + '\n' + text

print(text)

read_lines("Please insert row: ")

list.reverse()
print(list)
