from collections import deque

queue=deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.popleft()
queue.append(34)
queue.append(3)

print(queue)
queue.reverse() #역순으로 바꾸기
print(queue) #나중에 들어온 원소부터 출력
