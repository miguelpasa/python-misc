#########################################################################################################
# Problem 1:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#########################################################################################################

def isNumberMultipleOfThreeOrFive(x):
	return x % 3 == 0 or x % 5 == 0

sum = 0
belowThisNumber = 1000

for i in range(belowThisNumber):
	if isNumberMultipleOfThreeOrFive(i):
		sum += i

print(sum)
