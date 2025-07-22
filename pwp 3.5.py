def last_word_length(sentence):
    words = sentence.split()
    return len(words[-1])
sentence = input("Enter a sentence: ")
print("Length of last word:", last_word_length(sentence))


