# coding: utf-8
def fib(n):
	if n<2:
		return n
	else:
		return fib(n-1)+fib(n-2)

def f(L=None):
	if L is None:
		L = []
	L.append(42)
	return L

if __name__ == "__main__":

	f = open('Einkaufsliste','a')
	f2 = open('Einkaufsliste', 'r')
	f3 = open('Einkaufsliste', 'w')

	def pruefen():
		x = raw_input("Wollen Sie etwas zu Ihrer Liste hinzufügen, oder sie leeren?\n")

		if x ==	"hinzufügen":
			hinzu()
		elif x == "leeren":
			leeren()
		else:
			print("Bitte geben Sie hinzufügen oder leeren ein, um Ihre Liste zu bearbeiten.")
			pruefen()

	def hinzu():
		#Hinzufügen
		buy = raw_input("Was soll zur Einkaufsliste hinzugefügt werden?\n") 
		f.write(str(buy)+ '\n')
		string = f2.read()
		print("Auf Ihrer Einkaufsliste steht:\n")	
		print (string)

	def leeren():
		#Liste leeren
		f3.write("")
		print("Liste geleert")

	pruefen()
