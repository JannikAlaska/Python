# coding: utf-8


#------------------------------------------------------------------------------------------------
# Prüfung, was mit der Liste gemacht werden soll
#------------------------------------------------------------------------------------------------
def pruefen(): 
	x = raw_input("Wollen Sie etwas zu Ihrer Liste (h)inzufügen, oder sie (l)eeren?\n")

	if x ==	"h":
		hinzu()

	elif x == "l":
		leeren()

	else: #bei Falscheingabe wird die Abfrage nochmal ausgeführt
		print("Bitte gebenn Sie (h) oder (l) zum Hinzufügen oder Leeren ein.")
		pruefen()


#------------------------------------------------------------------------------------------------
# Hinzufügen
#------------------------------------------------------------------------------------------------

def hinzu():

	f = open('Einkaufsliste','r+')
	
	#buy- und read-Variablen füllen
	buy = raw_input("Was soll zur Einkaufsliste hinzugefügt werden?\n") 

	read1=f.read()
	wholeList = buy + read1

	#Hinzufügen der neuen Eingabe
	f.write(str(wholeList) + '\n')


	#Variablen wieder leeren
	buy = ""

	f.close()

	#Abfrage, ob weitere Einträge hinzugefügt werden sollen
	moreItems()

#------------------------------------------------------------------------------------------------
# Leeren
#------------------------------------------------------------------------------------------------

def leeren(): #Liste leeren

	f = open('Einkaufsliste','r+')

	f.truncate()
	print("Liste geleert")

#------------------------------------------------------------------------------------------------
# Mehr hinzufügen
#------------------------------------------------------------------------------------------------

def moreItems():


	#Abfrage, ob neuer Eintrag hinzugefügt werden soll
	more = raw_input("Wollen Sie noch etwas zur Liste hinzufügen? (j/n)")
	if more == "j":

		f = open('Einkaufsliste','r+')
		
		buymore = raw_input("Was soll zur Einkaufsliste hinzugefügt werden?\n")
		print("buymore: " + buymore) 
		
		#Hinzufügen zur Liste
		read2 = f.read()
		f.truncate()
		print("read2: " + read2)
		wholeList2 = str(buymore) + '\n' + str(read2)
		print("wholeList2: " + wholeList2)
		f.write(str(buymore) + '\n')

		f.close()

		#rekursiver Aufruf, bis etwas anderes, als "j" eingegeben wird
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

	

