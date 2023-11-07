def word_counter():
    different_words = set()
    lower_chars = list(map(chr, range(97, 123)))
    upper_chars = list(map(chr, range(65, 91)))
    chars_dict = {}
    for i in range(len(upper_chars)):
        chars_dict[upper_chars[i]] = lower_chars[i]
    with open('input.txt') as file:
        text = file.readlines()
        for line in text:
            for word in map(str, line.split()):
                corrected_symbols = []
                for symbol in word:
                    if symbol in lower_chars:
                        corrected_symbols.append(symbol)
                    elif symbol in upper_chars:
                        corrected_symbols.append(chars_dict[symbol])
                    elif symbol == "'":
                        corrected_symbols.append("'")
                different_words.add("".join(corrected_symbols))
    print(different_words)
    return len(different_words)


print(word_counter())





