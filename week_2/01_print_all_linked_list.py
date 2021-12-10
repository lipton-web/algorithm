# [3] -> [4]
# data, next
class Node:
	def __init__(self, data):
			self.data = data
			self.next = None

# node = Node(3)
# first_node = Node(4)
# node.next = first_node
# print(node.next.data)
# print(node.data)

class LinkedList:
	def __init__(self, data):
			self.head = Node(data)

	def append(self, data):
		if self.head is None:
			self.head = Node(data)
			return

		cur = self.head

		# 다음이 none이 아닐 때 까지 한칸씩 계속 이동
		while cur.next is not None:
			cur = cur.next
		cur.next = Node(data)

	def print_all(self):
		cur = self.head
		while cur is not None:
			print(cur.data)
			cur = cur.next

# [3] -> [4] -> [5] -> [6] -> None
linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()
# print(linked_list.head.data)