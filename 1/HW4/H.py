lengths = list(map(int, input().split()))
symbols = [*input()]
symbols_dict = dict()
word_dict = dict()
string = [*input()]
word = string[:lengths[0]]
symbols_occurrence = 0
for symbol in string:
    symbols_dict[symbol] = 0
    word_dict[symbol] = 0
for symbol in symbols:
    symbols_dict[symbol] += 1
for symbol in word:
    word_dict[symbol] += 1
if word_dict == symbols_dict:
    symbols_occurrence += 1
for symbol in string[lengths[0]:]:
    word.append(symbol)
    word_dict[symbol] += 1
    word_dict[word[0]] -= 1
    del word[0]
    if word_dict == symbols_dict:
        symbols_occurrence += 1
print(symbols_occurrence)
