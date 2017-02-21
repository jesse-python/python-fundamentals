def sumList(numList):
	theSum = 0
	for i in numList:
		theSum = i + theSum
	return theSum / len(numList)


print(sumList([1, 2, 5, 10, 255, 3]))
