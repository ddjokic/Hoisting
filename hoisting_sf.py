#!/usr/bin/env python

# calculates safety factor in hoisting lines with various number of parts & rotating sheaves
# (c) 2013, D. Djokic
# No guaranties, whatsoever - use code on your own risk
# Released under GNU General Public License

'''
	IADC safety factor recommendations:
		drilling and other routine operations = 3
		mast rising	= 2.5
		setting casing = 2
		jarring = 2
'''

def get_float(message, default):
#get float number - error check included
	try:
		f=input (message)
		st=type(f)
		if f==0:
			f=default
			return float(f) ##dodo
		elif f==" ":
			f=default
			return float(f)  ##dodo
		else:
			return float(f)
	except:
		print("Wrong Input! Try again")
		return(get_float(message, default))

def get_integer(message, default):
#get integer number - error check included
	try:
		f=input (message)
		st=type(f)
		if f==0:
			f=default
			return int(f)
		elif f==" ":
			f=default
			return int(f)
		else:
			return int(f)
	except:
		print("Wrong Input! Try again")
		return(get_integer(message, default))

def write_file (file, description, var):
#write to file
	file.write ("\n")
	file.write (str(description))
	file.write ("\t")
	file.write (str(var))

W = get_float ("Hoisted Weight in tones (1 ton = 2000lb) = ", 40)
L = get_float ("Capacity of existing wire rope in tones (1 ton = 2000lb): ", 90)
n = get_integer ("Number of lines or '0' for default of 4 = ", 4)
s = get_integer ("Number of rotating sheaves or '0' for equal to number of lines = ", n)
K = get_float ("Sheave roller bearing friction factor - enter '0' for default of 1.04 = ", 1.04)

print ("Wire line efficiency due to bending")
print ("1 - D/d ratio = 25:1 - API 9A")
print ("2 - D/d ratio = 40:1 - API 9A")
print ("3 - Input your data for wire line efficiency")
dratio = get_integer ("Choose 1, 2 or 3: ", 1)

if dratio == 1:
	wire_eff = 0.95
elif dratio == 2:
	wire_eff = 0.97
else:
	wire_eff = get_float ("Input wire line efficiency due to bending <1: ", 0.95)

sfact=L*wire_eff*(K**n-1)/((W*K**s)*(K-1))


fname = 'hoisting_sf.txt'
fn = open (fname, 'a')
fn.write ('hoisting_sf.py Output:')

print ("\n\nSafety Factor for Operation with this wire = %f" %(sfact))
print ("\nIADC Recommended Safety Factors:\n\nDrilling and other routine operations = 3\nMast Rising = 2.5\nSetting Casing = 2\nJarring = 2")

write_file (fn, "Hoisted weight in tones (1 ton = 2000 lb): ", W)
write_file (fn, "Capacity of existing wire rope in tones (1 ton = 2000lb): ", L)
write_file (fn, "Number of lines: ", n)
write_file (fn, "Number of rotating sheaves: " ,s)
write_file (fn, "Sheave roller bearing friction factor: ", K)
write_file (fn, "Wire Line Efficiency due to bending: ", wire_eff)
write_file (fn, "Safety Factor: ", sfact)
fn.write("\n\nIADC Recommended Safety Factors:")
fn.write ("\nDrilling and other routine operations = 3")
fn.write ("\nMast Rising = 2.5")
fn.write ("\nSetting Casing = 2")
fn.write ("\nJarring = 2")
fn.write ("\nValidate results! No any warranties are associated with this code!")
fn.close()
