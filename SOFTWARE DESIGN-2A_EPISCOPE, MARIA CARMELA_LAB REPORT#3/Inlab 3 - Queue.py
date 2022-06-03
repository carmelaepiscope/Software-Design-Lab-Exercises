#Implementation of queue using list
queue = []

queue.append('maria')
queue.append('carmela')
queue.append('episcope')
  
print("Initial queue")
print(queue)
 
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
  
print("\nQueue after removing elements")
print(queue)