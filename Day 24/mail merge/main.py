from hashlib import new


PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names= names_file.readlines()


with open("./Input/Letters/starting_letter.txt") as letter__file:
    content = letter__file.read()
    for name in names:
        stripped=name.strip()
        new_letter=content.replace(PLACEHOLDER,stripped)
        with open(f"./Output/ReadyToSend/letter_for_{stripped}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)