# myNumerology class for numerology.py

class myNumerology:
    def __init__(self):
        # paths definition
        self.path_dictionary = "./dict/eng_dict_boys.txt"
        self.path_dict_copy = "./dict/eng_dict_copy.txt"
        self.path_input_words = "./config/input_file.txt"
        self.path_n_to_find = "./config/numero_da_trovare.txt"
        self.path_numerology_type = "./config/numerology_type.num"
    
    def parse_input_file(self, infos):
        #infos is a unique string, self.signature is equal to every string before the first :
        self.signature = infos.split(':')[0]
        #instead, self.date is equal to every string after the first :
        self.date = infos.split(':')[1]
        self.day = self.date.split('/')[0]
        self.month = self.date.split('/')[1]
        self.year = self.date.split('/')[2]
    
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
    
    # setters and getters
    def set_signature(self, signature):
        self.signature = signature
    
    def get_signature(self):
        return self.signature
    
    def set_date(self, date):
        self.date = date
    
    def get_date(self):
        return self.date
    
    def set_day(self, day):
        self.day = day
    
    def get_day(self):
        return self.day
    
    def set_month(self, month):
        self.month = month
    
    def get_month(self):
        return self.month
    
    def set_year(self, year):
        self.year = year
    
    def get_year(self):
        return self.year
    
    
