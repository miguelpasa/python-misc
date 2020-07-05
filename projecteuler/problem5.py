#########################################################################################################
# Problem 5:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#########################################################################################################

def divisibleFromOneToTwenty(number):
	numberList = [11,12,13,14,15,16,17,18,19,20]
	for i in numberList:
		if number % i != 0:
			return bool(False)
	return bool(True)

counter = 20
while(1):
	if divisibleFromOneToTwenty(counter):
		print(counter, " is the smallest positive number that is evenly divisible.")
		exit()
		break
	counter = counter + 20
exit()