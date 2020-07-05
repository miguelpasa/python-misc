#####################################################################
# Problem 6:
# The sum of the squares of the first ten natural numbers is 385
# The square of the sum of the first ten natural numbers is 3025
#
# Hence the difference between the sum of the squares of the first 
# ten natural numbers and the square of the sum is 3025−385=2640.
#
# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.
#####################################################################

def findSumOfSquaresOfFirstOneHundredNumbers():
	sum = 0
	for i in range(1,101):
		sum = sum + i*i
	return sum

def findSquareOfSumOfFirstOneHundredNumbers():
	sum = 0
	for i in range(1,101):
		sum = sum + i
	return sum*sum

difference = findSquareOfSumOfFirstOneHundredNumbers() - findSumOfSquaresOfFirstOneHundredNumbers()
print("Difference is ", difference)