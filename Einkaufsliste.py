# coding: utf-8


#------------------------------------------------------------------------------------------------
# query what to do with the list
#------------------------------------------------------------------------------------------------
def pruefen(): 
	x = raw_input("Wollen Sie etwas zu Ihrer Liste (h)inzufügen, oder sie (l)eeren?\n")

	if x ==	"h":
		hinzu()

	elif x == "l":
		leeren()

	else: #restart the query in case of a wrong input
		print("Bitte gebenn Sie (h) oder (l) zum Hinzufügen oder Leeren ein.")
		pruefen()


#------------------------------------------------------------------------------------------------
# add
#------------------------------------------------------------------------------------------------

def hinzu():

	f = open('Einkaufsliste','r+')
	
	#fill the buy and read variables
	buy = raw_input("Was soll zur Einkaufsliste hinzugefügt werden?\n") 

	# // method1
	read1=f.read()
	wholeList = read1 + buy

	# add the new entry
	f.write(str(wholeList) + '\n')
	# // end method1


	# // method2
	# f.write(str(buy))
	# // end method2


	#empty the variables
	buy = ""

	f.close()

	#function to add more items to the list
	moreItems()

#------------------------------------------------------------------------------------------------
# empty
#------------------------------------------------------------------------------------------------

def leeren(): #Liste leeren

	f = open('Einkaufsliste','r+')

	f.truncate()
	print("Liste geleert")

#------------------------------------------------------------------------------------------------
# add more
#------------------------------------------------------------------------------------------------

def moreItems():


	#function to add more items to the list
	more = raw_input("Wollen Sie noch etwas zur Liste hinzufügen? (j/n)")
	if more == "j":

		f = open('Einkaufsliste','r+')
		
		buymore = raw_input("Was soll zur Einkaufsliste hinzugefügt werden?\n")
		print("buymore: " + buymore) 
		
		#add to the list
		read2 = f.read()
		f.truncate()
		print("read2: " + read2)
		wholeList2 = str(buymore) + '\n' + str(read2)
		print("wholeList2: " + wholeList2)
		f.write(str(buymore) + '\n')

		f.close()

		#recursive call until a 'j' is entered
		moreItems()


################################################################################################
# Main
################################################################################################

if __name__ == "__main__":



	pruefen()

	f = open('Einkaufsliste','r+')
	print("Auf Ihrer Einkaufsliste steht:\n")
	wholeList = f.read()
	print(wholeList)

	

