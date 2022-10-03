# myNumerology class for numerology.py

import utils as ut
import config.globals as glb
import json

class myNumerology(object):
	# def __init__(self):

	def parse_date(self):
		self.year = self.date[0:4]
		self.month = self.date[5:7]
		self.day = self.date[8:10]
	

	def get_all_json_data(self):
		
		#read json file and save in people all the data
		with open(glb.path_people_json) as f:
			d = json.load(f)
			people = d["people"]

		#loop through every person in people and save in this class all the data
		for person in people:
			#toupper because in json file can be in lower case
			#thus, not matching with the dictionary
			self.set_signature(people[person]["signature"].upper())
			self.set_date(people[person]["date"])
			self.parse_date()
	
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
	
  
	