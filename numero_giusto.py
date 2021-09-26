file_input_words = open("parole.txt", "r")
file_n_to_find = open("numero_da_trovare.txt", "r")
file_numerology_type = open("numerology_type.txt", "r")

n_tofind = file_n_to_find.read()
input_words_lower = file_input_words.read()
input_words = input_words_lower.upper()
number_table = file_numerology_type.read()

spl_new_line = number_table.split("\n")
line1_not_finished = spl_new_line[0]
line2_not_finished = spl_new_line[1]
line3_not_finished = spl_new_line[2]
line4_not_finished = spl_new_line[3]
line5_not_finished = spl_new_line[4]
line6_not_finished = spl_new_line[5]
line7_not_finished = spl_new_line[6]
line8_not_finished = spl_new_line[7]

line1 = line1_not_finished.split('=')
line2 = line2_not_finished.split('=')
line3 = line3_not_finished.split('=')
line4 = line4_not_finished.split('=')
line5 = line5_not_finished.split('=')
line6 = line6_not_finished.split('=')
line7 = line7_not_finished.split('=')
line8 = line8_not_finished.split('=')

line1_splitted = line1[1].split(" ")
line2_splitted = line2[1].split(" ")
line3_splitted = line3[1].split(" ")
line4_splitted = line4[1].split(" ")
line5_splitted = line5[1].split(" ")
line6_splitted = line6[1].split(" ")
line7_splitted = line7[1].split(" ")
line8_splitted = line8[1].split(" ")

n = 0

for letter in input_words:
	for letter_spl1 in line1_splitted:
		if (letter == letter_spl1):
			n+=1
	for letter_spl2 in line2_splitted:
		if (letter == letter_spl2):
			n+=2
	for letter_spl3 in line3_splitted:
		if (letter == letter_spl3):
			n+=3
	for letter_spl4 in line4_splitted:
		if (letter == letter_spl4):
			n+=4
	for letter_spl5 in line5_splitted:
		if (letter == letter_spl5):
			n+=5
	for letter_spl6 in line6_splitted:
		if (letter == letter_spl6):
			n+=6
	for letter_spl7 in line7_splitted:
		if (letter == letter_spl7):
			n+=7
	for letter_spl8 in line8_splitted:
		if (letter == letter_spl8):
			n+=8

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
