with open("Input/Letters/starting_letter.txt") as prototype:
    with open("Input/Names/invited_names.txt") as invited_names:
        all_names = invited_names.readlines()
        letter = prototype.read()
        for name in all_names:
            new_letter = letter.replace("[name]", name.strip())
            with open(f"Output/ReadyToSend/letter_for_{name.strip()}.docx", mode="w") as invitation:
                invitation.write(new_letter)
