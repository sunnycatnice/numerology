import utils as ut

file_input_words = open("./config/input_file.txt", "r")
file_n_to_find = open("./config/numero_da_trovare.txt", "r")
file_numerology_type = open("./config/numerology_type.txt", "r")
file_dictionary = open("./dict/ita_dictionary.txt", "r")

n_tofind = file_n_to_find.read()
input_words_lower = file_input_words.read()
input_words = input_words_lower.upper()
numbers_table = file_numerology_type.read()
dictionary_unparsed = file_dictionary.read()

table = ut.parse_numerology_file(numbers_table)
to_analyze = ut.parse_input_file(input_words)
signature = to_analyze[0]
day = to_analyze[1]
mohth = to_analyze[2]
year = to_analyze[3]
dictionary_indexed = ut.put_index_on_dictionary()

signature_integral = ut.count_nbrs_signature(signature, table)
signature_reduced = ut.reduce_numbers_uo_to_1000(signature_integral)
day_reduced = ut.reduce_numbers(day)
month_reduced = ut.reduce_numbers(mohth)
year_reduced = ut.reduce_numbers(year)
data_sum= day_reduced + month_reduced + year_reduced
data_sum_reduced = ut.reduce_numbers(data_sum)
karma = ut.reduce_numbers(data_sum_reduced)


print("\n[", signature, "] firma", signature_integral, "ridotta", signature_reduced)
print ("[", signature, "]", "è un", str(day_reduced) + "K" + str(karma), "con firma", signature_reduced, "\n")

#print(n_tofind)

#da aggiungere tipo 2K8 significa che...
#da aggiungere la lista di parole prese da un file e il numero desiderato...
#dunque aggiungere i suggerimenti di nomi
