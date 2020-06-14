word_count = 0

while True:
    line = input()
    if len(line) == 0:
        break

    word_count += len(line.split())

print(f"You typed {word_count} words")
