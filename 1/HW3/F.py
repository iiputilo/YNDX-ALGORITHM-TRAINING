string1 = input()
string2 = input()
dict_for_string1 = dict()
set_for_string2 = set()
for i in range(0, len(string1)-1):
    genome = string1[i] + string1[i+1]
    if genome in dict_for_string1:
        dict_for_string1[genome] += 1
    else:
        dict_for_string1[genome] = 1
for j in range(0, len(string2)-1):
    genome = string2[j] + string2[j + 1]
    set_for_string2.add(genome)
genome_relation_degree = 0
for genome in dict_for_string1:
    if genome in set_for_string2:
        genome_relation_degree += dict_for_string1[genome]
print(genome_relation_degree)
