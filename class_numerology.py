# myNumerology class for numerology.py

import parsing as prs
import utils as ut
import config.globals as glb
import json

class myNumerology(object):

	def __init__(self, person):
		#read json file and save in people all the data
		with open(glb.path_people_json) as f:
			d = json.load(f)
			people = d["people"]

		#toupper because in json file can be in lower case
		#thus, not matching with the dictionary
		self.set_name(people[person]["name"].upper())
		print(self.name)
		self.set_surname(people[person]["surname"].upper())
		self.set_signature(self.name + " " + self.surname)
		self.set_date(people[person]["date"])
		self.parse_date()

	def parse_date(self):
		self.year = self.date[0:4]
		self.month = self.date[5:7]
		self.day = self.date[8:10]

	def check_needed_number(self, day, karma_reduced):
		right_number_list = prs.parse_name_compatibility_file(glb.path_name_compatibility)
		day_and_karma = day + "K" + str(karma_reduced)

		right_numbers = ut.return_right_numbers(right_number_list, day_and_karma).split("-")
		return right_numbers

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

	def set_name(self, name):
		self.name = name
  
	def set_surname(self, surname):
		self.surname = surname
  
	def set_signature(self, signature):
		self.signature = signature
  
	def set_surname(self, surname):
		self.surname = surname

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
	
  
	