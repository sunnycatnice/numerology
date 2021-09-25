n_1 = "A I J Q Y"
n_2 = "B K R"
n_3 = "C G L S"
n_4 = "D M T"
n_5 = "E H N X"
n_6 = "U V W"
n_7 = "O Z"
n_8 = "F P"

file_auth_words = open("parole.txt", "r")
file_n_to_find = open("numero_da_trovare.txt", "r")

n_tofind = file_n_to_find.read()
auth_words_lower = file_auth_words.read()

auth_words = auth_words_lower.upper()

splitted_n_1 = n_1.split(" ")
splitted_n_2 = n_2.split(" ")
splitted_n_3 = n_3.split(" ")
splitted_n_4 = n_4.split(" ")
splitted_n_5 = n_5.split(" ")
splitted_n_6 = n_6.split(" ")
splitted_n_7 = n_7.split(" ")
splitted_n_8 = n_8.split(" ")

n = 0

for letter in auth_words:
	for letter_spl1 in splitted_n_1:
		if (letter == letter_spl1):
			n+=1
	for letter_spl2 in splitted_n_2:
		if (letter == letter_spl2):
			n+=2
	for letter_spl3 in splitted_n_3:
		if (letter == letter_spl3):
			n+=3
	for letter_spl4 in splitted_n_4:
		if (letter == letter_spl4):
			n+=4
	for letter_spl5 in splitted_n_5:
		if (letter == letter_spl5):
			n+=5
	for letter_spl6 in splitted_n_6:
		if (letter == letter_spl6):
			n+=6
	for letter_spl7 in splitted_n_7:
		if (letter == letter_spl7):
			n+=7
	for letter_spl8 in splitted_n_8:
		if (letter == letter_spl8):
			n+=8

#n_splitted = [int(a) for a in str(n)]
#n_reduced = 0

#for i in range(len(n_splitted)):
#	n_splitted = n_splitted +

#print("I numeri per la firma ", auth_words, " sono:", n, "\nIn riduzione il numero è: ", n_reduced)
print(n)

auth_words = auth_words.split(" ")
