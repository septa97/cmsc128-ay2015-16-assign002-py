#!/usr/bin/python3

import re

# Function for getting the hamming distance of two strings
def getHammingDistance(str1, str2):
	if (len(str1) != len(str2)):
		return -1

	hammingDistance = 0

	for i in range(len(str1)):
		if (str1[i] != str2[i]):
			hammingDistance += 1

	return hammingDistance



# Function for counting the overlapping substring pattern
def countSubstrPattern(original, pattern): 
	matches = re.findall(r'(?=%s)' % (pattern), original)

	count = 0
	for match in matches:
		count += 1

	return count



# Function for checking if a string is valid depending on the alphabet
def isValidString(str, alphabet):
	for char in str:
		if (char not in alphabet):
			return False

	return True



# Function for getting the skew
def getSkew(str, n):
	if (n <= 0):
		return 0

	G_Occurences = 0
	C_Occurences = 0

	for i in range(len(str)):
		if (i == n):
			break
			
		if (str[i] == "C"):
			C_Occurences += 1
		elif (str[i] == "G"):
			G_Occurences += 1

	return (G_Occurences - C_Occurences)



# Function for getting the maximum skew
def getMaxSkewN(str, n):
	if (n <= 0):
		return 0

	max = 0
	G_Occurences = 0
	C_Occurences = 0

	for i in range(len(str)):
		if (i == n):
			break
			
		if (str[i] == "C"):
			C_Occurences += 1
		elif (str[i] == "G"):
			G_Occurences += 1

		if (G_Occurences - C_Occurences > max):
			max = G_Occurences - C_Occurences

	return max



# Function for getting the minimum skew
def getMinSkewN(str, n):
	if (n <= 0):
		return 0

	min = 0
	G_Occurences = 0
	C_Occurences = 0

	for i in range(len(str)):
		if (i == n):
			break

		if (str[i] == "C"):
			C_Occurences += 1
		elif (str[i] == "G"):
			G_Occurences += 1
			if (G_Occurences == 1):
				min = 1

		if (G_Occurences - C_Occurences < min):
			min = G_Occurences - C_Occurences

	return min



# MAIN MENU
choice = True

while (choice != '0'):
	print ("\n\n\tMAIN MENU")
	print ("[1] getHammingDistance")
	print ("[2] countSubstrPattern")
	print ("[3] isValidString")
	print ("[4] getSkew")
	print ("[5] getMaxSkewN")
	print ("[6] getMinSkewN")
	print ("[0] EXIT\n\n")

	choice = input("What would you like to do? ")

	# If the choice is getHammingDistance
	if (choice == '1'):
		str1 = input("Enter the first string: ")
		str2 = input("Enter the second string: ")
		
		hammingDistance = getHammingDistance(str1, str2)

		if (hammingDistance != -1):
			print ("The hamming distance is", hammingDistance)
		else:
			print ("The length of the two strings are not equal!")

	# If the choice is countSubstrPattern
	elif (choice == '2'):
		original = input("Enter the string: ")
		pattern = input("Enter the pattern: ")

		print ("The number of overlapping substring pattern is", countSubstrPattern(original, pattern))

	# If the choice is isValidString
	elif (choice == '3'):
		string = input("Enter the string: ")
		alphabet = input("Enter the alphabet: ")

		if (isValidString(string, alphabet)):
			print ("The string IS valid.")
		else:
			print ("The string IS NOT valid.")

	# If the choice is getSkew
	elif (choice == '4'):
		string = input("Enter the string: ")
		n = input("Enter the value of n: ")

		if (int(n) >= 1):
			print ("The skew is", getSkew(string, int(n)))
		else:
			print ("You entered an invalid input for n. n must be greater than or equal to 1")

	# If the choice is getMaxSkewN
	elif (choice == '5'):
		string = input("Enter the string: ")
		n = input("Enter the value of n: ")

		if (int(n) >= 1):
			print ("The MAXIMUM skew is", getMaxSkewN(string, int(n)))
		else:
			print ("You entered an invalid input for n. n must be greater than or equal to 1")

	# If the choice is getMinSkewN
	elif (choice == '6'):
		string = input("Enter the string: ")
		n = input("Enter the value of n: ")

		if (int(n) >= 1):
			print ("The MINIMUM skew is", getMinSkewN(string, int(n)))
		else:
			print ("You entered an invalid input for n. n must be greater than or equal to 1")

	# If the choice is EXIT
	elif (choice == '0'):
		print ("Bye!")

	# Else, notify the user that his/her input is invalid
	else:
		print ("Please enter a valid input.")
