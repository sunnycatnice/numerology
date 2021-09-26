import utils as ut

file_input_words = open("input_file.txt", "r")
file_n_to_find = open("numero_da_trovare.txt", "r")
file_numerology_type = open("numerology_type.txt", "r")

n_tofind = file_n_to_find.read()
input_words_lower = file_input_words.read()
input_words = input_words_lower.upper()
numbers_table = file_numerology_type.read()

table = ut.parse_numerology_file(numbers_table)
to_analyze = ut.parse_input_words(input_words)

n = 0

for letter in input_words:
	for letter_spl1 in table[0]:
		if (letter == letter_spl1):
			n+=1
	for letter_spl2 in table[1]:
		if (letter == letter_spl2):
			n+=2
	for letter_spl3 in table[2]:
		if (letter == letter_spl3):
			n+=3
	for letter_spl4 in table[3]:
		if (letter == letter_spl4):
			n+=4
	for letter_spl5 in table[4]:
		if (letter == letter_spl5):
			n+=5
	for letter_spl6 in table[5]:
		if (letter == letter_spl6):
			n+=6
	for letter_spl7 in table[6]:
		if (letter == letter_spl7):
			n+=7
	for letter_spl8 in table[7]:
		if (letter == letter_spl8):
			n+=8
  for letter_spl9 in table[8]:
    if (letter == letter_spl9):
      n+=9

n_splitted = [int(a) for a in str(n)]
n_reduced = 0
n_tmp = 0

#non funziona se deve ridurre numeri sopra a 1000....
if (len(n_splitted) >= 2):
	for i in n_splitted:
		n_reduced+=i
	tmp = [int(a) for a in str(n_reduced)]
	if (len(tmp) >= 2):
		for i in tmp:
			n_tmp+=i
		n_reduced = n_tmp

print("\nI numeri per la firma", input_words, "sono:", n)
if (n_reduced != 0):
	print("In riduzione il numero è:", n_reduced, "\n")

#da aggiungere tipo 2K8 che con firma ... significa che.... (quindi anche date)
#da aggiungere la lista di parole prese da un file e il numero desiderato...
#poi aggiungere i suggerimenti di nomi
