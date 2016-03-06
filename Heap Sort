#We define a function whre we give an array as input and it returns us a Heap
def  Heapify(Y):

	N = len(Y)

	if N%2 == 0:
		Y.append(float("-inf"))

	N = len(Y)

	k = (N+1)/2
	

	while 1:

		k = k-1
		
		if k == 0:
			break
		else:
			j = k
			

			while 1:

				s = 2*j
				if Y[s-1] < Y[s-1+1]:
					
					s = s+1
				else:
					pass
				if Y[s-1] > Y[j-1]:
					temp = Y[s-1]
					Y[s-1] = Y[j-1]
					Y[j-1] = temp
					if 2*s > N:
						break
					else:
						j = s
						continue
				else:
					break

	return Y





Y = [12, 66, 38, 9, 65, 61, 37, 47, 14, 85, 99, 54, 92, 2, 47, 23, 90, 11, 65, 40, 13, 43, 51, 76]
H = []
N = len(Y)


print 'The Original array is given by:\n', Y

#In every iteration the following block will generate heap from array and we replace the first element with -inf
#After every iteration we store the root of the heap
for j in range(N):
	
	Y = Heapify(Y)
	# Adding the root of the heap to Array H
	H.append(Y[0]) 
	Y[0] = float("-inf")


print 'The array after sorting is given by: \n',H
