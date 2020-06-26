# coding: utf-8

class MyClass:
	#Klassenvariablen
	zahl = 42
	string = "zeichenkette"

	#Konstruktor: Variablen können übergeben werden (beim Erzeugen der Instanz) oder wie hier mit Defaultwert (='a') belegt werden
	def __init__(self, buchstabeneu='a'):
		#Instanzvariablen
		self.buchstabe = buchstabeneu

	def do_something(self, neuezahl):
		# self. ist nötig um Variable zahl nicht als locale Variable in der Funktion do_something zu betrachten, sodnern um auf die Klassenvariable zahl, welche aktuell 42 ist, zuzugreifen 
		self.zahl = neuezahl

#Erzeugen einer neuen Instanz der Klasse MyClass. Bedeutet: Klasse ist z.B. Golf 7 mit feststehenden Merkmalen (Farbe, Motor,...). Instanz ist mein Golf, der Golf des Nachbarn,...
instanz = MyClass('z')
#Instanzvariablen können sich pro Instanz unterscheiden, Klassenvariablen aber gelten für alle Instanzen einer Klasse
instanz2 = MyClass('x')
instanz.do_something(1337)
print(instanz2.buchstabe)
