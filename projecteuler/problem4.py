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

print(isNumberAPalindrome(10222224201))

for num in range (998001, 0, -1):
	if isNumberAPalindrome(num):
		print(num, " has been the largest so far")
		exit()