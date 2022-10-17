import sys
import parsing as prs
import utils as ut
import config.globals as glb
from class_numerology import myNumerology

file_numerology_type = open(glb.path_numerology_type, "r")
numbers_table = file_numerology_type.read()

# general dictionary part, to be moved in a separate file
person = myNumerology("person0")

dict_len = ut.count_file_lenght(glb.path_dictionary)
line_parsed = prs.parse_dict(glb.path_dict_copy)
table = prs.parse_numerology_file(numbers_table)

# Person class part (to iterate in the future for CLI or make API)
person.set_dictionary_length(dict_len)
person.set_line_parsed(line_parsed)
person.set_table(table)

person.set_numerology_signature_integral(ut.count_nbrs_signature(person.signature, person.table))
person.set_numerology_signature_reduced(ut.reduce_numbers_up_to_1000(person.numerology_signature_integral))
person.set_day(ut.reduce_numbers(person.day))
person.set_month = ut.reduce_numbers(person.month)
person.set_year = ut.reduce_numbers(person.year)
person.set_karma_complete(person.day + person.month + person.year)
person.set_karma_reduced(ut.reduce_numbers_up_to_1000(person.karma_complete))

ut.generate_copied_upper_file(person.table)
ut.count_nbrs_dict(dict_len, line_parsed, person.table, glb.path_dict_copy, bool_entire = True)
numbers_to_find = person.check_needed_number(person.day, person.karma_reduced)
ut.generate_out_file_multiple_numbers(dict_len, glb.path_dict_copy, numbers_to_find)

print("\n[", person.signature, "] firma", person.numerology_signature_integral, "ridotta", person.numerology_signature_reduced)
print ("[", person.signature, "]", "è un", person.day + "K" + str(person.karma_reduced), "con firma", person.numerology_signature_reduced, "\n")
print("Le firme giuste per", person.day + "K" + str(person.karma_reduced), "sono:", numbers_to_find)
print("Firme generate in output.txt")
print("")


#da aggiungere tipo 2K8 significa che...
#da aggiungere la lista di parole prese da un file e il numero desiderato...
#dunque aggiungere i suggerimenti di nomi
# to add file json compatibility
