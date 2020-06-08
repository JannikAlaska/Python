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
		print("Bitte geben Sie hinzufügen oder leeren ein, um Ihre Liste zu bearbeiten.")
		pruefen()


#------------------------------------------------------------------------------------------------
# Hinzufügen
#------------------------------------------------------------------------------------------------

def hinzu():

	buy = raw_input("Was soll zur Einkaufsliste hinzugefügt werden?\n") 
	read1 = f.read()
	wholeList = str(buy) + '\n' + str(read1)
	f.write(str(wholeList))
	read1 = ""
	buy = ""
	wholeList = ""
	moreItems()

#------------------------------------------------------------------------------------------------
# Leeren
#------------------------------------------------------------------------------------------------

def leeren(): #Liste leeren

	f.truncate(0)
	print("Liste geleert")

#------------------------------------------------------------------------------------------------
# Mehr hinzufügen
#------------------------------------------------------------------------------------------------

def moreItems():
	more = raw_input("Wollen Sie noch etwas zur Liste hinzufügen? (j/n)")
	if more == "j":
		buymore = raw_input("Was soll zur Einkaufsliste hinzugefügt werden?\n") 
		f.write(str(buymore) + '\n')
		moreItems()


################################################################################################
# Main
################################################################################################

if __name__ == "__main__":

	f = open('Einkaufsliste','r+')

	pruefen()


	print("Auf Ihrer Einkaufsliste steht:\n")
	wholeList = f.read()
	print(wholeList)

	

