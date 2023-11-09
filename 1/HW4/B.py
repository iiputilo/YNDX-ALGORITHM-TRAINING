with open('input.txt') as file:
    text = file.read().split()
    words = dict()
    encountered_words = []
    for word in text:
        if word not in words:
            words[word] = 0
            encountered_words.append(str(0))
        else:
            words[word] += 1
            encountered_words.append(str(words[word]))
    print(*encountered_words)
