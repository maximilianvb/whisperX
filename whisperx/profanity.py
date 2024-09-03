from profanity_check import predict, predict_prob
import string
import os

def build_set_profanities():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'profanity_wordlist.txt')
    with open(file_path, 'r') as file:
        return set(word.strip().lower() for word in file)

set_comp = build_set_profanities()
def remove_compounds(segments, compound_words):
    
    # Convert compound words to lowercase and remove punctuation
    compound_words_cleaned = compound_words.lower().translate(str.maketrans('', '', string.punctuation))
    compound_words_set = set(compound_words_cleaned.split())
    
    # Iterate over each segment and replace compounded words
    for segment in segments:
        # Convert text to lowercase and remove punctuation
        text = segment['text']
        text_no_punct = text.lower().translate(str.maketrans('', '', string.punctuation))
        
        words = text_no_punct.split()
        for i, word in enumerate(words):
            # Check if the word is in the compounded swearing set
            # if we want to support more languages we need a swearing set, probably...
            if word in set_comp or predict([word])[0]:
                print('profanity', word)
                # Skip if the word is an exact match with any word in compound_words_set
                if word in compound_words_set:
                    continue
                
                # Find all substrings from compound_words_set that are in the word
                substrings = sorted([sub for sub in compound_words_set if sub in word], key=len, reverse=True)
                
                if substrings:
                    # Split the word based on all found substrings
                    parts = []
                    last_end = 0
                    for substring in substrings:
                        start = word.index(substring, last_end)
                        if start > last_end:
                            parts.append(word[last_end:start])
                        parts.append(substring)
                        last_end = start + len(substring)
                    if last_end < len(word):
                        parts.append(word[last_end:])
                    
                    # Remove empty parts and join with spaces
                    replacement = ' '.join(filter(bool, parts))
                    
                    # Replace in text_no_punct
                    text_no_punct = text_no_punct.replace(word, replacement, 1)
                    print(f"Replaced '{word}' with '{replacement}'")
        
        # Update the segment text with the modified version
        segment['text'] = text_no_punct
    
    return segments