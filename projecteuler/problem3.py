#########################################################################################################
# Problem 3:
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#########################################################################################################

largestPrimeFactor = 0
largestPrimeFactorOfThisNumber = 600851475143

def isNumberPrimeNumber(number):
	isPrimeNumber = bool(True)
	for loop in range(2, number, 1):
			if number % loop == 0 and loop < number:
				isPrimeNumber = bool(False)

	if isPrimeNumber:
		print("prime")
		return bool(True)
	else:
		print("not prime")
		return bool(False)

for i in range(1, int(largestPrimeFactorOfThisNumber/2) + 1, 1):
	if largestPrimeFactorOfThisNumber % i == 0:
		print("asdasdasdasd")
		if isNumberPrimeNumber(i):
			largestPrimeFactor = i
	print(largestPrimeFactor)