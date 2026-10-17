from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        zeroStudents = len([i for i in students if i == 0])
        oneStudents = len(students) - zeroStudents
        stuCount = [zeroStudents, oneStudents]
        
        for s in sandwiches:
            if stuCount[s] > 0:
                stuCount[s] -= 1
            else:
                break

        return sum(stuCount)

        # question to answer: 
        # 1. How many zero students are not fed?
        # 2. How many one students are not fed?
