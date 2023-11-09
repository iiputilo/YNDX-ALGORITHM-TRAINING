lower_chars = list(map(chr, range(97, 123)))
upper_chars = list(map(chr, range(65, 91)))
upper_to_lower = dict()
lower_to_upper = dict()
for i in range(len(upper_chars)):
    upper_to_lower[upper_chars[i]] = lower_chars[i]
for i in range(len(upper_chars)):
    lower_to_upper[lower_chars[i]] = upper_chars[i]
num_of_words = int(input())
dictionary = []
for _ in range(num_of_words):
    dictionary.append(input())
words = input().split()
mistakes = 0
for word in words:
    if word not in dictionary:
        up_chars_cnt = 0
        up_char_indices = []
        for x in range(len(word)):
            if word[x] in upper_chars:
                up_chars_cnt += 1
                up_char_indices.append(x)
        if up_chars_cnt > 1:
            mistakes += 1
        elif up_chars_cnt == 0:
            mistakes += 1
        elif up_chars_cnt == 1:
            word_in_dict = False
            left_part = word[:up_char_indices[0]]
            right_part = word[up_char_indices[0]+1:]
            char_list = []
            for char in left_part:
                char_list.append(char)
            char_list.append(upper_to_lower[word[up_char_indices[0]]])
            for char in right_part:
                char_list.append(char)
            for i in range(len(word)):
                char_list[i] = lower_to_upper[char_list[i]]
                if ''.join(char_list) in dictionary:
                    word_in_dict = True
                char_list[i] = upper_to_lower[char_list[i]]
            if word_in_dict:
                mistakes += 1
print(mistakes)
