#!/usr/bin/env python

# calculates allowable hoisting capacity of drilling lines with various number of parts & rotating sheaves
# (c) 2013, D. Djokic
# No guaranties, whatsoever - use code on your own risk
# Released under GNU General Public License

''' L=W*K**s*(K-1)/(K**n-1)
	W - hoisted weight
	n - number of lines
	s - number of rotating sheaves - usually, equal to n, unless there are more than one
	fastline sheave or split crown is used
	K = 1.04 sheave roller bearing friction factor
	wire line efficiency due to bending, per API 9A:
		0.95 for 25:1 D/d ratio
		0.97 for 40:1 D/d ratio

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
n = get_integer ("Number of lines or '0' for default of 4 = ", 4)
s = get_integer ("Number of rotating sheaves or '0' for equal to number of lines = ", n)
K = get_float ("Sheave roller bearing friction factor - enter '0' for default of 1.04 = ", 1.04)

print ("Type of operation - safety factors: ")
print ("1 - Drilling and other routine operations")
print ("2 - Mast rising")
print ("3 - Setting casing")
print ("4 - Jarring")
op = get_integer ("Choose 1,2,3 or 4: ", 1)

if op==1:
	sf =3.0
elif op==2:
	sf == 2.5
else:
	sf == 2.0

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

Lton = (W*K**s)*(K-1)/(K**n-1)
L1ton = Lton*sf/wire_eff
L1lb = L1ton*2000

fname = 'hoisting.txt'
fn = open (fname, 'a')
fn.write ('hoisting.py Output:')
write_file (fn, "Safety factor: ", sf)
write_file (fn, "Wire line efficiency due to bending: ", wire_eff)
write_file (fn, "Hoisted weight in tones (1 ton = 2000 lb): ", W)
write_file (fn, "Number of lines (parts): ", n)
write_file (fn, "Number of rotating sheaves: ", n)
write_file (fn, "Sheave roller bearing friction factor: ", K)
write_file (fn, "Minimum required wire capacity [tones]: ", L1ton)
write_file (fn, "Minimum required wire capacity [lb]: ", L1lb)
fn.write ("\n")
fn.write ("There is no any kind of guaranties associated to results of this script! Validate results!")
fn.close ()
print ("Minimum required wire capacity [ton] = %f" %(L1ton))
print ("Minimum required wire capacity [lb] = %f" %(L1lb))
print ("Check file 'IADC_hoisting.txt' in working folder!")
print ("Job done!")