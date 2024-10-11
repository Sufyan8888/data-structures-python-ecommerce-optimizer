from collections import deque

# Creating a queue for order processing
order_queue = deque()

# Adding (enqueue) orders to the queue
order_queue.append("Order 1")
order_queue.append("Order 2")
order_queue.append("Order 3")

# Displaying current orders in the queue
print("Current orders in the queue:", list(order_queue))

# Processing (dequeue) the first order in the queue
print("Processing:", order_queue.popleft())  # Processes Order 1
print("Remaining orders in the queue:", list(order_queue))  # Remaining orders

# Adding a new order
order_queue.append("Order 4")
print("Updated orders in the queue:", list(order_queue))
