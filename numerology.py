import parsing as prs
import utils as ut
from class_numerology import myNumerology
# import time

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

person.generate_copied_upper_file()
dict_len = ut.count_file_lenght(person.path_dictionary)
line_parsed = prs.parse_dict(person.path_dict_copy)
table = prs.parse_numerology_file(numbers_table)

person.set_dictionary_length(dict_len)
person.set_line_parsed(line_parsed)
person.set_table(table)
person.count_nbrs_dict()

ut.generate_out_file(dict_len, person.path_dict_copy, n_tofind)

person.set_signature_integral(ut.count_nbrs_signature(person.signature, table))
person.set_signature_reduced(ut.reduce_numbers_up_to_1000(person.signature_integral))
person.set_day(ut.reduce_numbers(person.day))
person.set_month = ut.reduce_numbers(person.month)
person.set_year = ut.reduce_numbers(person.year)
person.set_karma_complete(person.day + person.month + person.year)
person.set_karma_reduced(ut.reduce_numbers_up_to_1000(person.karma_complete))

print("\n[", person.signature, "] firma", person.signature_integral, "ridotta", person.signature_reduced)
print ("[", person.signature, "]", "è un", person.day + "K" + str(person.karma_reduced), "con firma", person.signature_reduced, "\n")

#da aggiungere tipo 2K8 significa che...
#da aggiungere la lista di parole prese da un file e il numero desiderato...
#dunque aggiungere i suggerimenti di nomi
# to add file json compatibility
