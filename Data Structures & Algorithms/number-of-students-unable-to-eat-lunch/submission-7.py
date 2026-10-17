from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        zeroStudents = len([i for i in students if i == 0])
        oneStudents = len(students) - zeroStudents
        stuCount = [zeroStudents, oneStudents]
        prevLen = 0
        sammys = deque(sandwiches)

        while prevLen is not len(sammys) and len(sammys) > 0:
            prevLen = len(sammys)
            currSand = sammys[0]
            if stuCount[currSand] >= 1:
                stuCount[currSand] -= 1
                sammys.popleft()

        return sum(stuCount)

        # 0 0 1 1 1 1 
        # 0 0 0 1 1 1

        # question to answer: 
        # 1. How many zero students are not fed?
        # 2. How many one students are not fed?
