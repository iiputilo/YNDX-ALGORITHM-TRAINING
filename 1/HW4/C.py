with open('input.txt') as file:
    text = file.read().split()
    words = dict()
    unique_words = set()
    for word in text:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
        unique_words.add(word)
    unique_words = sorted(unique_words)
    count_words = []
    for word in unique_words:
        count_words.append(words[word])
    max_cnt = max(count_words)
    for x in range(len(unique_words)):
        if count_words[x] == max_cnt:
            print(unique_words[x])
            break
