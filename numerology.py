import parsing as prs
import utils as ut
from class_numerology import myNumerology

# to add file json compatibility!!!!
person = myNumerology()

file_input_words = open(person.path_input_words, "r")
file_n_to_find = open(person.path_n_to_find, "r")
file_numerology_type = open(person.path_numerology_type, "r")

n_tofind = file_n_to_find.read()
input_words_lower = file_input_words.read()
input_words = input_words_lower.upper()
numbers_table = file_numerology_type.read()

person.parse_input_file(input_words)
table = prs.parse_numerology_file(numbers_table)

person.generate_copied_upper_file()
dict_len = ut.count_file_lenght(person.path_dictionary)
line_parsed = prs.parse_dict(person.path_dict_copy)
ut.count_nbrs_dict(dict_len, line_parsed, table, person.path_dict_copy)
ut.generate_out_file(dict_len, person.path_dict_copy, n_tofind)

signature_integral = ut.count_nbrs_signature(person.signature, table)
signature_reduced = ut.reduce_numbers_up_to_1000(signature_integral)
person.set_day(ut.reduce_numbers(person.day))
month_reduced = ut.reduce_numbers(person.month)
year_reduced = ut.reduce_numbers(person.year)
data_sum= person.day + month_reduced + year_reduced
karma = ut.reduce_numbers_up_to_1000(data_sum)

print("\n[", person.signature, "] firma", signature_integral, "ridotta", signature_reduced)
print ("[", person.signature, "]", "è un", person.day + "K" + str(karma), "con firma", signature_reduced, "\n")

#da aggiungere tipo 2K8 significa che...
#da aggiungere la lista di parole prese da un file e il numero desiderato...
#dunque aggiungere i suggerimenti di nomi
# to add file json compatibility
