import parsing as prs
import utils as ut
from class_numerology import myNumerology

# general dictionary part, to be moved in a separate file
person = myNumerology()

file_n_to_find = open(person.path_n_to_find, "r")
file_numerology_type = open(person.path_numerology_type, "r")

n_tofind = file_n_to_find.read()
numbers_table = file_numerology_type.read()

dict_len = ut.count_file_lenght(person.path_dictionary)
line_parsed = prs.parse_dict(person.path_dict_copy)
table = prs.parse_numerology_file(numbers_table)
ut.generate_copied_upper_file(table)

ut.count_nbrs_dict(dict_len, line_parsed, table, person.path_dict_copy)
ut.generate_out_file(dict_len, person.path_dict_copy, n_tofind)

# Person class part (to iterate in the future for CLI or make API)
person.get_all_json_data()
person.set_dictionary_length(dict_len)
person.set_line_parsed(line_parsed)
person.set_table(table)

person.set_numerology_signature_integral(ut.count_nbrs_signature(person.signature, table))
person.set_numerology_signature_reduced(ut.reduce_numbers_up_to_1000(person.numerology_signature_integral))
person.set_day(ut.reduce_numbers(person.day))
person.set_month = ut.reduce_numbers(person.month)
person.set_year = ut.reduce_numbers(person.year)
person.set_karma_complete(person.day + person.month + person.year)
person.set_karma_reduced(ut.reduce_numbers_up_to_1000(person.karma_complete))

print("\n[", person.signature, "] firma", person.numerology_signature_integral, "ridotta", person.numerology_signature_reduced)
print ("[", person.signature, "]", "è un", person.day + "K" + str(person.karma_reduced), "con firma", person.numerology_signature_reduced, "\n")

#da aggiungere tipo 2K8 significa che...
#da aggiungere la lista di parole prese da un file e il numero desiderato...
#dunque aggiungere i suggerimenti di nomi
# to add file json compatibility
