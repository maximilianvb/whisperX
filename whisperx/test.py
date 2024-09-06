from profanity import remove_compounds

test_data = [{'text': ' Hello, this is a test video. Motherfucker. Bitches. Fuck. Fuck you. Asshat. Shitface. Dogshit.', 'start': 0.913, 'end': 12.261}]

final = remove_compounds(test_data, "shit ass fuck motherfucker bitch")
print(final)
