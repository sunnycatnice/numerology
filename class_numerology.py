# myNumerology class for numerology.py

class myNumerology:
    def __init__(self):
        # paths definition
        self.path_ita_dictionary = "./dict/eng_dict.txt"
        self.path_ita_dict_indexed = "./dict/ita_dic_indexed.txt"
        self.path_input_words = "./config/input_file.txt"
        self.path_n_to_find = "./config/numero_da_trovare.txt"
        self.path_numerology_type = "./config/numerology_type.txt"
    
    def parse_input_file(self, infos):
        #infos is a unique string, self.signature is equal to every string before the first :
        self.signature = infos.split(':')[0]
        #instead, self.date is equal to every string after the first :
        self.date = infos.split(':')[1]
        self.day = self.date.split('/')[0]
        self.month = self.date.split('/')[1]
        self.year = self.date.split('/')[2]
