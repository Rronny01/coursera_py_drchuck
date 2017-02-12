# This first line is provided for you
try:
	inp = raw_input("Enter Hours:")
	hrs = float(inp)
	inp = raw_input("Enter Rate:")
	rate = float(inp)
except:
	print "Error, please enter numeric input"
	
print rate, hrs
if hrs <= 40 :
	pay = rate * hrs
else :
	pay = rate * 40 + (rate * 1.5 * (hrs - 40))
print pay