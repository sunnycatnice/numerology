from shutil import copyfile

def reduce_numbers(day):
	n_reduced = 0
	day_splitted = [int(a) for a in str(day)]

	if (len(day_splitted) >= 2):
		for digit in day_splitted:
			n_reduced+=digit

	return str(n_reduced)

def reduce_numbers_up_to_1000(n):
	n_reduced = 0
	n_tmp = 0
	n_splitted = [int(a) for a in str(n)]
	if (int(n) > 9):
		if (len(n_splitted) >= 2):
			for i in n_splitted:
				n_reduced+=i
			tmp = [int(a) for a in str(n_reduced)]
			if (len(tmp) >= 2):
				for i in tmp:
					n_tmp+=i
				n_reduced = n_tmp
	else:
		n_reduced = n
	return n_reduced

def count_nbrs_signature(signature, table):
	n = 0
	for letter in signature:
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
	return (n)

def put_index_on_dictionary(filepath_ita_dictionary):
	index = 1
	filepath_ita_dict_indexed = "./dict/ita_dic_indexed.txt"

	copyfile(filepath_ita_dictionary, filepath_ita_dict_indexed)

	with open(filepath_ita_dict_indexed, "r") as fp:
		lines_upper = fp.read().upper()
		lines = lines_upper.splitlines()
	with open(filepath_ita_dict_indexed, "w") as fp:
		for line in lines:
			print(str(index) , line, file=fp)
			index += 1
	return index

def count_nbrs_dict(dict_len, line_parsed, table, filepath_ita_dict_indexed):

	#do numerology
	i = 0
	to_reduce = [None] * dict_len
	while(i < (dict_len - 1)):
		to_reduce[i] = count_nbrs_signature(line_parsed[i][1], table)
		i += 1
	
	#reduce numbers
	i = 0
	to_append = [None] * dict_len
	while (i < (dict_len - 1)):
		to_append[i] = reduce_numbers_up_to_1000(to_reduce[i])
		i += 1

	#write changes on file
	i = 0
	with open(filepath_ita_dict_indexed, "r") as fp:
		lines_not_splitted = fp.read()
		lines = lines_not_splitted.splitlines()
	with open(filepath_ita_dict_indexed, "w") as fp:
		for line in lines:
			print (line , str(to_append[i]), file=fp)
			i += 1

def generate_out_file(dict_len, table, filepath_ita_dict_indexed, n_tofind):

	with open(filepath_ita_dict_indexed, "r") as fp:
		lines_not_splitted = fp.read()
		lines_to_split_spaces = lines_not_splitted.splitlines()
		i = 0
		line_splitted = [None] * dict_len
		with open(filepath_ita_dict_indexed, "r") as fp:
			for line in lines_to_split_spaces:
				line_splitted[i] = line.split(" ")
				i += 1
		
		i = 0
		j = 0
		while (i < (dict_len - 1)):
			if (line_splitted[i][2] == n_tofind):
				j += 1
			i += 1

	print (n_tofind[0])
	print (line_splitted[3])
	right_number = [None] * j
	i = 0
	j = 0
	while (i < (dict_len - 1)):
		if (line_splitted[i][2] == n_tofind):
			right_number[j] = line_splitted[i]
			j += 1
		i += 1

	i = 0
	print (right_number[i])
	with open("./outfile.txt", "w") as fp:
		for line in right_number:
			#unire la lista con join e stampare la linea
			print(right_number[i], file=fp)
			i += 1