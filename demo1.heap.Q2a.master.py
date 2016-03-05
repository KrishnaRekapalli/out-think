

Y = [12, 66, 38, 9, 65, 61, 37, 47, 14, 85, 99, 54, 92, 2, 47, 23, 90, 11, 65, 40, 13, 43, 51, 76]

N = len(Y)

# If the size of the array is even we add -inf to the array to make the number of elements odd
if N%2 == 0:
	Y.append(float("-inf"))

print 'The original array is given by:\n',Y


N = len(Y)
k = (N+1)/2

while 1:
	#Step 2
	k = k-1
	
	if k == 0:
		break
	else:
		j = k

		#step 3
		while 1:

			s = 2*j
			# Here we compare the values of children. We have to make sure that
			# The value of the parent is greater than the maximum of the children
			# As this is a max heap
			if Y[s-1] < Y[s-1+1]:
				
				s = s+1
			else:
				pass
			if Y[s-1] > Y[j-1]:
			#Now if the max of children has a vlaue higer than the parent,
			# then we will swap the values of parent and that child

				#Step 4
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


print 'The array Y after performing Heap Sort is given by: \n',Y


