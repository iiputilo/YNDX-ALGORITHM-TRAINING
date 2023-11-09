upper_chars = list(map(chr, range(65, 91)))
num_of_words = int(input())
dictionary = []
dictionary_lower = []
for _ in range(num_of_words):
    input_word = input()
    dictionary.append(input_word)
    dictionary_lower.append(input_word.lower())
words = input().split()
mistakes = 0
for word in words:
    if word.lower() in dictionary_lower and word not in dictionary:
        mistakes += 1
    else:
        upper_char_count = 0
        for char in word:
            if char in upper_chars:
                upper_char_count += 1
                if upper_char_count > 1:
                    break
        if upper_char_count > 1:
            mistakes += 1
        elif upper_char_count == 0:
            mistakes += 1
print(mistakes)
