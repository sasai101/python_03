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
#normale Funktion
def test(a,b):
	a+b
	
result1 = test(11,22)
print("result1 = %s"%result1)

#unnormal Funktion
func = lambda a,b:a+b

result2 = func(11,22)
print("result2 = %s"%result2)

#in normale Funktion muss man return schreiben damit die Losung auskommen  kann. Lambda nicht.
#lambda Funktion ist nur fuer einfache Rechnung.

def test1(a,b,func):
	result = func(a,b)
	print("result = %s"%result)

test1(11,22,lambda x,y:x+y)
test1(11,22,lambda x,y:x-y)
test1(11,22,lambda x,y:x*y)
test1(11,22,lambda x,y:x/y)
