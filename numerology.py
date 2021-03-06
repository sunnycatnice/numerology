import parsing as prs
import utils as ut

filepath_ita_dictionary = "./dict/ita_dictionary.txt"
filepath_ita_dict_indexed = "./dict/ita_dic_indexed.txt"
filepath_input_words = "./config/input_file.txt"
filepath_n_to_find = "./config/numero_da_trovare.txt"
filepath_numerology_type = "./config/numerology_type.txt"

file_input_words = open(filepath_input_words, "r")
file_n_to_find = open(filepath_n_to_find, "r")
file_numerology_type = open(filepath_numerology_type, "r")


n_tofind = file_n_to_find.read()
input_words_lower = file_input_words.read()
input_words = input_words_lower.upper()
numbers_table = file_numerology_type.read()

table = prs.parse_numerology_file(numbers_table)
to_analyze = prs.parse_input_file(input_words)
signature = to_analyze[0]
day = to_analyze[1]
mohth = to_analyze[2]
year = to_analyze[3]
dict_len = ut.put_index_on_dictionary(filepath_ita_dictionary)
line_parsed = prs.parse_dict(filepath_ita_dict_indexed)
ut.count_nbrs_dict(dict_len, line_parsed, table, filepath_ita_dict_indexed)
ut.generate_out_file(dict_len, table, filepath_ita_dict_indexed, n_tofind)

signature_integral = ut.count_nbrs_signature(signature, table)
signature_reduced = ut.reduce_numbers_up_to_1000(signature_integral)
day_reduced = ut.reduce_numbers(day)
month_reduced = ut.reduce_numbers(mohth)
year_reduced = ut.reduce_numbers(year)
data_sum= day_reduced + month_reduced + year_reduced
karma = ut.reduce_numbers_up_to_1000(data_sum)

print("\n[", signature, "] firma", signature_integral, "ridotta", signature_reduced)
print ("[", signature, "]", "è un", str(day_reduced) + "K" + str(karma), "con firma", signature_reduced, "\n")

#da aggiungere tipo 2K8 significa che...
#da aggiungere la lista di parole prese da un file e il numero desiderato...
#dunque aggiungere i suggerimenti di nomi
