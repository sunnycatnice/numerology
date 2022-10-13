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

  ret = (line1_splitted, line2_splitted, line3_splitted, line4_splitted, line5_splitted, line6_splitted, line7_splitted, line8_splitted, line9_splitted)

  return ret

def parse_dict(filepath_dict_copy):
	index = 0
	mtx_len = 0

	with open(filepath_dict_copy) as fp:
		lines = fp.read().splitlines()
	with open(filepath_dict_copy, "r") as fp:
		for line in lines:
			mtx_len += 1
	fp.close()
 
	line_splitted = [None] *mtx_len
	with open(filepath_dict_copy, "r") as fp:
		for line in lines:
			line_splitted[index] = line.split(" ")
			# print(str(index) + str(line_splitted[index]))
			index += 1
	fp.close()
	return (line_splitted)

# It returns a list of lists containing:
# In the first position the day & karma 
# & in the second position the corresponding right numbers
def parse_name_compatibility_file(filepath_name_compatibility):
	index = 0
	mtx_len = 0

	#count the number of lines in the file
	with open(filepath_name_compatibility) as fp:
		lines = fp.read().splitlines()
	with open(filepath_name_compatibility, "r") as fp:
		for line in lines:
			mtx_len += 1
	fp.close()
 
	#save the lines in a matrix
	line_splitted = [None] *mtx_len
	with open(filepath_name_compatibility, "r") as fp:
		for line in lines:
			line_splitted[index] = line.split(" ")
			index += 1
	fp.close()
	
	#split every touple in the matrix by the "=" sign and save the result in a new matrix
	line_splitted_by_equal_sign = [None] *mtx_len
	for i in range(0, mtx_len):
		line_splitted_by_equal_sign[i] = line_splitted[i][0].split("=")
	return (line_splitted_by_equal_sign)