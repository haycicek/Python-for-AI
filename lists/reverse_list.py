words = []
while True:
    word = input("Enter a word (or type 'done' to finish): ")# sample: 9 8 7 6 5 4 3 2 1 -> 1 2 3 4 5 6 7 8 9
    if word.lower() == 'done':
        break
    words.append(word)

words.reverse()
print("Words in reverse order:")
for word in words:
    print(word)
