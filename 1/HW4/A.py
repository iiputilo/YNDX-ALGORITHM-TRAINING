num = int(input())
dict1 = dict()
dict2 = dict()
for _ in range(num):
    word1, word2 = input().split()
    dict1[word1] = word2
    dict2[word2] = word1
synonym = input()
try:
    print(dict1[synonym])
except KeyError:
    print(dict2[synonym])
