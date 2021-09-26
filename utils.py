
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

  ret = [line1_splitted, line2_splitted, line3_splitted, line4_splitted, line5_splitted, line6_splitted, line7_splitted, line8_splitted]

  return ret 
