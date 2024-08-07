# Task 1
# Design a stack-based data structure to represent the kitchen's order queue, where orders are processed in the order they are received.

# Task 2
# Implement functions to add new orders to the kitchen's order queue and remove orders when they are completed.

# Task 3

# Design a queue-based data structure to represent the customer order queue, where orders are prioritized based on factors such as customer waiting time and order complexity.
# Task 4

# Implement functions to add new orders to the customer order queue, process orders, and notify customers when their orders are ready for pickup or delivery.

def line():
    print('~'*30)

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class OrderQueue():
    def __init__(self):
        self.head = None
        self.tail = None

    # function to add orders to queue
    def enqueue(self,orderdata):
        new_order = Node(orderdata)
        if self.head == None:
            self.head = new_order 
            self.tail = new_order
        else:
            self.tail.next = new_order
            self.tail = new_order

    #traversing the order,to represent the kitchen's order queue, to display orders in the order they are received 
    def order_display(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def dequeue(self):
        if self.head == None:
            return "There are no orders left !!All others processed"
        else:
            order = self.head # remove the head
            self.head = self.head.next # reassign the title of head to hat comes next
            return order.data # return the severed head

order_queue = OrderQueue()
order_queue.enqueue("Avacado Roll")
order_queue.enqueue("Paneer Sandwich")
order_queue.enqueue("Jalapeno Bagel with Salsa Shmear")
order_queue.enqueue("Nachos with Dip")
order_queue.enqueue("Hot Chocolate Pizookie")
order_queue.enqueue("Bluberry Cheesecake Ice cream")

line()

print("Orders placed in the kitchen stack:")

order_queue.order_display()

line()

print("Orders : extra item added")

line()

order_queue.enqueue("Deep Dish Pizza")

order_queue.order_display()

line()

print("Following Order has been completed:")

order_val = order_queue.dequeue()

print(order_val)

line()

print("Remaining orders:")
line()
order_queue.order_display()


class NodeNew():
    def __init__(self,order,wait_time,order_complexity):
        self.order=order
        self.wait_time = wait_time
        self.order_complexity = order_complexity
        self.next=None

class Cust_Order_Queue():
    def __init__(self):
        self.head = None
        self.tail = None

    # function to add orders to queue
    def enqueue(self,order,wait_time,order_complexity):
        new_order = NodeNew(order,wait_time,order_complexity)
        if self.head == None:
            self.head = new_order 
            self.tail = new_order
        else:
            self.tail.next = new_order
            self.tail = new_order

    #traversing the order,to represent the kitchen's order queue, to display orders in the order they are received 
    def order_display(self):
        cur = self.head
        while cur:
            print(f"Order: {cur.order} with wait time: {cur.wait_time} and order complexity: {cur.order_complexity}")
            cur = cur.next

    def to_list(self):
        result=[]
        cur = self.head
        while cur:
            result.append(cur)
            cur = cur.next
        return result 
    
    def from_list(self,nodes):
        for item in nodes:
            self.enqueue(item.order,item.wait_time,item.order_complexity)
    
    def sort_orders_by_wait_time(self):
        nodes = self.to_list()
        nodes.sort(key=lambda x : x.wait_time)
        self.head = None
        self.tail = None
        self.from_list(nodes)
        #print(sorted_list)

    def sort_orders_by_complexity(self):
        nodes= self.to_list()
        nodes.sort(key=lambda x : x.order_complexity)
        self.head = None
        self.tail = None
        self.from_list(nodes)

    def dequeue(self):
        if self.head == None:
            return "There are no orders left !!All others processed"
        else:
            order = self.head # remove the head
            self.head = self.head.next # reassign the title of head to hat comes next
            return f"Order: {order.order} with wait time: {order.wait_time} and order complexity: {order.order_complexity} is completed"


cust_order_queue = Cust_Order_Queue()
cust_order_queue.enqueue("Avacado Roll",10,7)
cust_order_queue.enqueue("Paneer Sandwich",20,5)
cust_order_queue.enqueue("Jalapeno Bagel with Salsa Shmear",20,6)
cust_order_queue.enqueue("Nachos with Dip",20,3)
cust_order_queue.enqueue("Hot Chocolate Pizookie",30,8)
cust_order_queue.enqueue("Bluberry Cheesecake Ice cream",35,9)

line()

print("customer Orders placed:")

line()

cust_order_queue.order_display()

line()

print("customer Orders : extra item added")

line()

cust_order_queue.enqueue("Deep Dish Pizza",15,6)

cust_order_queue.order_display()

line()

print("Following Customer Order has been completed:")

line()

order_val = cust_order_queue.dequeue()

print(order_val)

line()

print("Remaining orders:")
line()
cust_order_queue.order_display()

line()

print("Sorted Queue contents: Based on order complexity")
cust_order_queue.sort_orders_by_complexity()

line()

cust_order_queue.order_display()

line()

print("Sorted Queue contents: Based on wait time")
line()
cust_order_queue.sort_orders_by_wait_time()

cust_order_queue.order_display()