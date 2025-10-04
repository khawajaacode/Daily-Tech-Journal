queue = []

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue after enqueue:", queue)

# Dequeue
print("Dequeued element:", queue.pop(0))
print("Queue after dequeue:", queue)

# Peek
print("Front element:", queue[0])

# Check if empty
if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")
