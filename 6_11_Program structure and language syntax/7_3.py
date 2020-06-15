sentence = input("Enter sentence: ")

for word in sentence.split():
    print("Word: ", word)
    print("First letter is:", word[0])
    print(f"The word has {len(word)} characters")
