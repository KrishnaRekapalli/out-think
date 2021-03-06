class Element(object):

	def __init__(self, value):

		self.value = value
		self.next = None



class LinkedList(object):

	def __init__(self,head=None):
		self.head = head


	def append(self,new_element):

		current = self.head

		if self.head:

			while current.next:

				current = current.next

			current.next = new_element

		else:

			self.head = new_element


	def get_position(self,position):

		current = self.head

		if position < 0:

			return None

		elif position == 0:

			return current

		elif position > 0:

			for i in range(position-1):
				current = current.next

				if current == None:
					return None

			return current

	def insert(self,new_element,position):

		current = self.head

		if position == 1:

			self.head = new_element
			new_element.next = current

			pass

		elif position ==2:

			linkBreak = current
			oldLink = current.next

			linkBreak.next = new_element
			new_element.next = oldLink

			pass




		elif position >2 :


			for i in range(1,position-1):
				current = current.next

			linkBreak = current

			oldLink = current.next

			linkBreak.next = new_element
			new_element.next = oldLink

			pass

	def delete(self,value):

		current = self.head

		if current.value == value:

			self.head = current.next

			pass


		else:

			while current.value != value:

				prevLink = current
				current = current.next

			prevLink.next = current.next

			pass





# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value


# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value


# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value

