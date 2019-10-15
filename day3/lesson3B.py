#Arithmetic Operation
#=====================
#date: 10/10/19
#---------------------

try:
	x = int(input("Enter x : "))
	y = int(input("Enter y : "))
	
	print (x+y)
	print (x-y)
	print (x/y)
	print (x%y)
	print (x**y)

except ZeroDivisionError as ex1 :
    print (ex1)
except:
	print ("enter a valid number!!!")

