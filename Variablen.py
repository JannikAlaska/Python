# coding: utf-8


# ---Funktionen----------------------------------------------------------------------------------------------------

def f():
	def local():
		x = "local text"
	def do_nonlocal():
		nonlocal x
		x = "nonlocal text"
	def do_global():
		global x
		x = "global text"
	x = "test"
	local()
	do_nonlocal()
	print("after init: " + x)

# ---Variablen-----------------------------------------------------------------------------------------------------

# ---Main----------------------------------------------------------------------------------------------------------
if __name__ = "__main__":
	f()
	print("global: " + var)
