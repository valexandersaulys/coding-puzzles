# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
		# Case our doubley linked list is empty
		if not self.head and not self.tail:
			self.head = node
			self.tail = node
			return
		
		# Loop until we find our new node
		new_head = node
        placeholder = self.head
		while placeholder:
			# while iterating, stop if we see this node already
			if placeholder == new_head: # .value?
				tmp_prev = placeholder.prev
				tmp_next = placeholder.next
				if tmp_prev:
					placeholder.prev.next = tmp_next
				if tmp_next:
					placeholder.next.prev = tmp_prev
				break
			placeholder = placeholder.next
		
		# Set our new head equal to the passed node
		self.head, self.head.next, self.head.prev = new_head, self.head, None
		# make sure the old head points to our new head
		self.head.next.prev = self.head
		return

    def setTail(self, node):
		# Case of empty linked list
        if not self.head and not self.tail:
			self.head = node
			self.tail = node
			return
		
		# Loop through until we find our node -- this time going backwards
		new_tail = node  
		placeholder = self.tail
		while placeholder:
			# like for setHead but with tails
			if placeholder == new_tail:
				placeholder.prev.next, placeholder.next.prev = placeholder.next, placeholder.prev
				break
			placeholder = placeholder.prev
			
		# set our new tail equal to the passed node
		self.tail, self.tail.next, self.tail.prev = new_tail, None, self.tail
		self.tail.prev.next = self.tail
		return

    def insertBefore(self, node, nodeToInsert):
		if not self.head and not self.tail:
			return False  # empty list, nothing to insert
		
		placeholder = self.head
		while placeholder:
			if placeholder == node:
				tmp_prev = placeholder.prev
				tmp_next = placeholder

				# Case: we're at the beginning of our Doubley Linked list
				if tmp_prev:
					placeholder.prev.next = nodeToInsert
				else:
					self.head = nodeToInsert
					
				placeholder.prev = nodeToInsert
				placeholder.prev.next = placeholder
				placeholder.prev.prev = tmp_prev
				break
			
			placeholder = placeholder.next
		return

    def insertAfter(self, node, nodeToInsert):
		if not self.head and not self.tail:
			return False  # empty list, nothing to insert
		
		placeholder = self.head
		while placeholder:
			if placeholder == node:
				tmp_prev = placeholder
				tmp_next = placeholder.next
				
				# Case: we're at the end of the double linked list
				if tmp_next != None:
					placeholder.next.prev = nodeToInsert
					
				placeholder.next = nodeToInsert
				placeholder.next.prev = placeholder
				placeholder.next.next = tmp_next
				
				if tmp_next == None:
					self.tail = placeholder.next
				
				return;
			
			placeholder = placeholder.next
		return

    def insertAtPosition(self, position, nodeToInsert):
        """position is 1 indexed""" 
		# Case if its an empty linked list
		if self.head == self.tail == None:
			self.head = nodeToInsert
			self.tail = nodeToInsert
			return
		
		index = 1
		placeholder = self.head
		while placeholder:
			if index == position:
				tmp_prev = placeholder.prev
				tmp_next = placeholder.next
				
				if tmp_prev:
					placeholder.prev.next = nodeToInsert
					
				if tmp_next:
					placeholder.next.prev = nodeToInsert
					
				placeholder = nodeToInsert
				return
			index += 1
			placeholder = placeholder.next
		return

    def removeNodesWithValue(self, value):
		if self.head == None and self.tail == None:
			return 
		
        # case of single value in our linked list
		if self.head == self.tail and self.head.value == value:
			self.head = None
			self.tail = None
			return
		
		placeholder = self.head
		while placeholder:
			if placeholder.value == value:
				tmp_prev = placeholder.prev
				tmp_next = placeholder.next
				if tmp_prev:
					placeholder.prev.next = tmp_next
				
				if tmp_next:
					placeholder.next.prev = tmp_prev
				break
			placeholder = placeholder.next
		return

    def remove(self, node):
        # Case of single value in our linked list
		if self.head == self.tail and self.head == node:
			self.head = None
			self.tail = None
			return
		
		#print("remove %d" % node.value)
		placeholder = self.head
		while placeholder:
			if placeholder == node:
				tmp_prev = placeholder.prev
				tmp_next = placeholder.next
				if tmp_prev:
					placeholder.prev.next = tmp_next   
				if tmp_next:
					placeholder.next.prev = None
					
				if node == self.head:
					self.head = tmp_next
				if node == self.tail:
					self.tail = tmp_prev
				break
			placeholder = placeholder.next
		return

    def containsNodeWithValue(self, value):
		if self.head == None and self.tail == None:
			return False
      	# Write your code here.
		placeholder = self.head
		while placeholder:
			if placeholder.value == value:
				return True
			placeholder = placeholder.next
		return False
