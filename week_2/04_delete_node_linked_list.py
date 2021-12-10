class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value) #새로운 노드
        if index == 0:
            new_node.next = self.head #[6] -> [5]
            self.head = new_node # head -> [6] -> [5] -> ...
            return

        node = self.get_node(index -1) #index - 1번째 노드 가져오기(앞에 추가 해야 되서 -1)
        next_node = node.next # next_node는 현재 노드의 다음꺼
        node.next = new_node # node.next의 다음꺼는 new_node
        new_node.next = next_node #new_node의 다음꺼 next_node
        return

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return

        node = self.get_node(index -1)
        node.next = node.next.next
        return
        



linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.add_node(2, 6)
# linked_list.delete_node(0)
# linked_list.get_node(0) # -> 5를 들고 있는 노드를 반환해야 합니다!
# print(linked_list.get_node(2).data)
linked_list.print_all()