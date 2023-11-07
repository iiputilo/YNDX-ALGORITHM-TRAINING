def word_counter():
    with open('input.txt') as file:
        text = file.readlines()
        different_words = set()
        for line in text:
            for word in map(str, line.split()):
                different_words.add(word)
        return len(different_words)


print(word_counter())
