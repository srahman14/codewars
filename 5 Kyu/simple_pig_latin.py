# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !



def pig_it(text):
    words = text.split()
    newWords = []

    for word in words:
        if word.isalpha():
            new_word = word[1:] + word[0] + "ay"
        else:
            new_word = word
        
        newWords.append(new_word)
    
    return " ".join(newWords)

print(pig_it('Pig latin is cool'))
