def parse_numerology_file(number_table):
  spl_new_line = number_table.split("\n")
  line1_not_finished = spl_new_line[0]
  line2_not_finished = spl_new_line[1]
  line3_not_finished = spl_new_line[2]
  line4_not_finished = spl_new_line[3]
  line5_not_finished = spl_new_line[4]
  line6_not_finished = spl_new_line[5]
  line7_not_finished = spl_new_line[6]
  line8_not_finished = spl_new_line[7]
  line9_not_finished = spl_new_line[8]

  line1 = line1_not_finished.split('=')
  line2 = line2_not_finished.split('=')
  line3 = line3_not_finished.split('=')
  line4 = line4_not_finished.split('=')
  line5 = line5_not_finished.split('=')
  line6 = line6_not_finished.split('=')
  line7 = line7_not_finished.split('=')
  line8 = line8_not_finished.split('=')
  line9 = line9_not_finished.split('=')

  line1_splitted = line1[1].split(" ")
  line2_splitted = line2[1].split(" ")
  line3_splitted = line3[1].split(" ")
  line4_splitted = line4[1].split(" ")
  line5_splitted = line5[1].split(" ")
  line6_splitted = line6[1].split(" ")
  line7_splitted = line7[1].split(" ")
  line8_splitted = line8[1].split(" ")
  line9_splitted = line9[1].split(" ")

  ret = [line1_splitted, line2_splitted, line3_splitted, line4_splitted, line5_splitted, line6_splitted, line7_splitted, line8_splitted, line9_splitted]

  return ret 

def parse_input_file(input_words):
	spl_colon = input_words.split(":")
	spl_slash = spl_colon[1].split("/")
	day = spl_slash[0]
	month = spl_slash[1]
	year = spl_slash[2]
	
	err = 0
	if (day.isnumeric() == False):
		err += 1
	if (month.isnumeric() == False):
		err += 20
	if (year.isnumeric() == False):
		err += 30
	
	if (err != 0):
		if (err == 1):
			exit("Error in: day date")
		if (err == 20):
			exit("Error in: month date")
		if (err == 30):
			exit("Error in: year date")
		if (err == 21):
			exit("Error in: day && month date")
		if (err == 31):
			exit("Error in: day && year date")
		if (err == 50):
			exit("Error in: month && year date")
		if (err == 51):
			exit("Error in the WHOLE date")

	if ((int)(day) > 31):
		exit("Error: the days can't be more than 31...")
	if ((int)(month) > 12):
		exit("Error: the months can't be more than 12...")
	if ((int)(year) < -5000 or (int)(year) > 5000):
		exit("Error: ain't you thinking too much babe? Check the year")
	ret = [spl_colon[0], day, month, year]

	return ret

def reduce_numbers(day):
	n_reduced = 0
	day_splitted = [int(a) for a in str(day)]

	if (len(day_splitted) >= 2):
		for digit in day_splitted:
			n_reduced+=digit

	return n_reduced

def reduce_numbers_uo_to_1000(n):
	n_reduced = 0
	n_tmp = 0
	n_splitted = [int(a) for a in str(n)]
	if (len(n_splitted) >= 2):
		for i in n_splitted:
			n_reduced+=i
		tmp = [int(a) for a in str(n_reduced)]
		if (len(tmp) >= 2):
			for i in tmp:
				n_tmp+=i
			n_reduced = n_tmp
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