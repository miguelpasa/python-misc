#########################################################################################################
# Problem 7:
# By listing the first six prime numbers: 
#        
#            2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
#########################################################################################################
import miguelutils

counter = 2
primeNumbersEncountered = 0

while(primeNumbersEncountered <= 10000):
	if miguelutils.isNumberPrimeNumber(counter):
		primeNumbersEncountered = primeNumbersEncountered + 1
	else:
		counter = counter + 1

print("The answer is ", counter)