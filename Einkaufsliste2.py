# coding: utf-8


#------------------------------------------------------------------------------------------------
# query what to do with the list
#------------------------------------------------------------------------------------------------
def pruefen(): 
	x = raw_input("Was wollen Sie mit Ihrer Einkaufsliste tun? \n(a) - Ansehen \n(h) - Hinzufügen \n(b) - Bearbeiten \n(x) - Löschen\n(l) - Leeren \n(q) - Abbrechen\n")

	if x == "a":
		file2list(True)

	elif x == "h":
		hinzu()

	elif x == "b":
		bearbeiten()

	elif x == "x":
		delete()

	elif x == "l":
		leeren()

	elif x == "q":
		return "ok"

	else: #restart the query in case of a wrong input
		print("\n \nBitte gebenn Sie (h) oder (l) zum Hinzufügen oder Leeren ein.")
		pruefen()

	return x


#------------------------------------------------------------------------------------------------
# add
#------------------------------------------------------------------------------------------------

def hinzu():

	again = "j"

	while again == "j":

		f = open('Einkaufsliste','r+')
		again=""
		
		#fill the buy and read variables
		buy = raw_input("\n \nWas soll zur Einkaufsliste hinzugefügt werden?\n") 

		# fill wholeList
		read1=f.read()
		wholeList = read1 + buy

		# add entry to file
		f.write(str(buy) + '\n')


		f.close()


		#empty the variables
		buy = ""
		read1=""
		wholeList=""



		again = raw_input("\n \nSoll noch etwas Zur Liste Hinzugefügt werden?(j/n)")
		

		#function to add more items to the list
		#moreItems()

#------------------------------------------------------------------------------------------------
# empty
#------------------------------------------------------------------------------------------------

def leeren(): #Liste leeren

	f = open('Einkaufsliste','r+')

	f.truncate()
	print("\n \nListe geleert")



#------------------------------------------------------------------------------------------------
# edit
#------------------------------------------------------------------------------------------------

def bearbeiten(): # Liste bearbeiten
	
	liste = file2list()
	edit_nr=0

	edit_nr = input("\n \nWelcher Eintrag soll bearbeitet werden?\n")
	edit_value = raw_input("\n \nWas soll statt dessen an dieser Stelle stehen?\n")

	edit_nr = edit_nr - 1

	f = open ("Einkaufsliste", "r+")
	f.truncate()

	liste[edit_nr] = edit_value

	for w in liste:	
		f.write(str(w) + '\n')



#------------------------------------------------------------------------------------------------
# delete
#------------------------------------------------------------------------------------------------

def delete(): # delete entry
	
	liste = file2list()
	del_nr=0

	del_nr = input("\n \nWelcher Eintrag soll gelöscht werden?\n")

	del_nr = del_nr - 1

	f = open ("Einkaufsliste", "r+")

	del liste[del_nr]

	f.truncate()

	for w in liste:	
		f.write(str(w)+ '\n')


#------------------------------------------------------------------------------------------------
# file2list
#------------------------------------------------------------------------------------------------

def file2list(justview):

	f = open('Einkaufsliste','r')
	liste = []
	print("\n \nAuf Ihrer Einkaufsliste steht:\n")
	#wholeList = f2.read()

	for line in f:
		liste.append(line.strip())

	i=1	
	for w in liste:
		print (str(i) + " - " + str(w))
		i = i + 1
	print("\n")

	if justview == True:
		pruefen()

	return liste


#------------------------------------------------------------------------------------------------
# viewlist
#------------------------------------------------------------------------------------------------	




################################################################################################
# Main
################################################################################################

if __name__ == "__main__":

	x = pruefen()

	if x != "a":
		viewlist()

	# print(liste)

		

