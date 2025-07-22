def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)
sentence = input("Enter a sentence: ")
print("Longest word:", longest_word(sentence))


