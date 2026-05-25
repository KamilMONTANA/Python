
names_tab = []

with open("./Input/Names/invited_names.txt", "r") as names:
    for line in names:
        names_tab.append(line.strip())

print(names_tab)
letters = []
for name in names_tab:
    with open("./Input/Letters/starting_letter.txt", "r") as letter:
        letter = letter.read()
        new_letter = letter.replace("[name]", name)
        letters.append(new_letter)


for i in range(len(letters)):
    with open(f"./Output/ReadyToSend/{names_tab[i]}.txt", "w") as ready:
        ready.write(letters[i])

