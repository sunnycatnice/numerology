# myNumerology class for numerology.py

import utils as ut
import json

class myNumerology(object):
	def __init__(self):
		# paths definitions for dictionaries
		self.path_dictionary = "./dictionaries/input_dictionaries/eng_dict_boys.txt"
		self.path_dict_copy = "./dictionaries/output_dictionaries/eng_dict_copy.txt"
		# path definitions for configs
		self.path_people_json = "./config/people.json"
		self.path_n_to_find = "./config/numero_da_trovare.txt"
		self.path_numerology_type = "./config/numerology_type.num"

	def parse_date(self):
		self.year = self.date[0:4]
		self.month = self.date[5:7]
		self.day = self.date[8:10]
	

	def get_all_json_data(self):
		
		#read json file and save in people all the data
		with open(self.path_people_json) as f:
			d = json.load(f)
			people = d["people"]

		#loop through every person in people and save in this class all the data
		for person in people:
			#toupper because in json file can be in lower case
			#thus, not matching with the dictionary
			self.set_signature(people[person]["signature"].upper())
			self.set_date(people[person]["date"])
			self.parse_date()

	#file manipulation
	def generate_copied_upper_file(self):
		index = 0
		file = open(self.path_dictionary, "r")
		filecopy = open(self.path_dict_copy, "w")
		for line in file:
			if line != "\n":
				#print without a \n
				print(line.upper(), file=filecopy, end="",)
				index += 1
		file.close()
		filecopy.close()
 
	def count_nbrs_dict(self):

		#do numerology
		i = 0
		to_reduce = [None] * self.dict_len
		while(i < (self.dict_len)):
			to_reduce[i] = ut.count_nbrs_signature(self.line_parsed[i], self.table)
			i += 1

		#reduce numbers
		i = 0
		to_append = [None] * self.dict_len
		while (i < (self.dict_len - 1)):
			to_append[i] = ut.reduce_numbers_up_to_1000(to_reduce[i])
			i += 1

		#write changes on file
		i = 0
		with open(self.path_dict_copy, "r") as fp:
			lines_not_splitted = fp.read()
			lines = lines_not_splitted.splitlines()
		with open(self.path_dict_copy, "w") as fp:
			for line in lines:
				print (line , str(to_append[i]), file=fp)
				i += 1
	
	def set_dictionary_length(self, dict_len):
		self.dict_len = dict_len
	
	def set_line_parsed(self, line_parsed):
		self.line_parsed = line_parsed
  
	def set_table(self, table):
		self.table = table
  
	def set_numerology_signature_integral(self, numerology_signature_integral):
		self.numerology_signature_integral = numerology_signature_integral
  
	def set_numerology_signature_reduced(self, numerology_signature_reduced):
		self.numerology_signature_reduced = numerology_signature_reduced
  
	def set_signature(self, signature):
		self.signature = signature

	def set_date(self, date):
		self.date = date
	
	def set_day(self, day):
		self.day = day
	
	def set_month(self, month):
		self.month = month
  
	def set_year(self, year):
		self.year = year
	
	def set_karma_complete(self, karma_complete):	
		self.karma_complete = karma_complete

	def set_karma_reduced(self, karma_reduced):
		self.karma_reduced = karma_reduced
	
  
	