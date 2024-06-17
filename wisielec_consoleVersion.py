import random

my_file = open("sgb-words.txt", "r")
data = my_file.read()
words = data.split("\n")

word = random.choice(words)

find_word = ['_' for i in range(len(word))]
lifes = 5
print(find_word)
print(f'You have {lifes} lifes.')
while True and lifes > 0:
    w = input('Podaj litere:')
    if w in word:
        for i in range(len(word)):
            if w == word[i]:
                find_word[i] = w
        print(find_word)
    else:
        print("Nie ma litery w slowie")
        print(find_word)
        lifes -= 1
        print(f'You have {lifes} lifes.')

    if find_word == [*word]:
        print("YEEAH! You find the world")
        break
    if lifes == 0:
        print(f'Word is: {word}.')
        break
