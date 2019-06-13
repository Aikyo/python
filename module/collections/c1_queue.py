import collections
q1 = collections.deque(maxlen=3)
q1.append([1,2])
q1.append(1)
q1.append(3)
q1.append(4)
#a = q1.pop()
print(q1)
#print(a)

import queue
q2 = queue.Queue()
q2.put("a")
q2.put("b")

print(q2.get())
print(q2)





