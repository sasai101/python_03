# eine normale Funktion
#def Funktion():
#	pass

# eine unnormale Funktion
'''
lambda canshi:shizi

bianliang = lambda x,y:x+y
Also ein Attributte ist eine Funktion.

zum Beispiel
'''
def test(a,b,func):
	result = func(a,b)
	print(result)

func_new = input("bitte geben Sie eine Funktion ein : ")
func_new = eval(func_new)  # Funktion von eval ist string to funktion
test(11,22,func_new)
