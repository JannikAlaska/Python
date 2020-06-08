# coding: utf-8

# Geg.: Temperatur in Grad Celsius C
# Ges.: Temperatur in Grad Kelvin K
# K = C + 273.15


def Temp_input():

	while True:
		C = input("Gib die Temperatur in Grad Celsius ein: ")
		try:
			C = float (C)
			return C

		except ValueError:
			return error

def calc(C):

	K = C + 273.15
	return K



if __name__ == "__main__":
	print (Temp_input())
	C = Temp_input()
	if C == "error":
		print("Das ist keine gültige Angabe für eine Temperatur.")

	print ("Das sind " + str(calc(C)) + " Kelvin.")
