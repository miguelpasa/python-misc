#########################################################################################################
# @param  number to check if is primt
# @return true if number is a prime number, false if it isn't a prime number
#########################################################################################################
def isNumberPrimeNumber(number):
	isPrimeNumber = bool(True)
	for loop in range(2, number, 1):
			if number % loop == 0 and loop < number:
				isPrimeNumber = bool(False)

	if isPrimeNumber:
		return bool(True)
	else:
		return bool(False)