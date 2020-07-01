#########################################################################################################
# Problem 4:
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is
#
#           9009 = 91 × 99
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#########################################################################################################

def isNumberAPalindrome(number):
	lengthOfNumber = len(str(number))
	for i in range (0, int(lengthOfNumber/2)+1):
		if str(number)[i] != str(number)[-(i+1)]:
			return bool(False)
	return bool(True)

largestNumberSoFar = 0
for firstThreeDigitNumber in range (100, 1000, 1):
	for secondThreeDigitNumber in range (100, 1000, 1):
		product = firstThreeDigitNumber*secondThreeDigitNumber
		if isNumberAPalindrome(product):
			if product > largestNumberSoFar:
				largestNumberSoFar = product
				print(firstThreeDigitNumber, " * ", secondThreeDigitNumber, " = ", firstThreeDigitNumber*secondThreeDigitNumber)

print(largestNumberSoFar)