# First In First Out 이라고 해서 FIFO

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):  # enqueue(data) : 맨 뒤에 데이터 추가하기 
        # 어떻게 하면 될까요?
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):  # dequeue() : 맨 앞의 데이터 뽑기
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "Queue is Empty"

        delete_head = self.head
        self.head = self.head.next
        return delete_head.data

    def peek(self): # peek() : 맨 앞의 데이터 보기
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "Queue is Empty"

        return self.head.data

    def is_empty(self): # isEmpty(): 큐가 비었는지 안 비었는지 여부 반환해주기
        # 어떻게 하면 될까요?
        return self.head is None

queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())