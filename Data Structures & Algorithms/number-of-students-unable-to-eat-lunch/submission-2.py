from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sammys = deque(sandwiches)
        sinceLastPop = 0

        while sinceLastPop is not len(students):
            if students[0] == sammys[0]:
                sinceLastPop = 0
                students.popleft()
                sammys.popleft()
                continue
            curr = students.popleft()
            students.append(curr)
            sinceLastPop += 1

        return len(students)