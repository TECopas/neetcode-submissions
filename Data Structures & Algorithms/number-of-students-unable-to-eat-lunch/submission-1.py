class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = collections.deque(students)
        res = len(students)
        cycle = 0
        cycleDetector = len(students)
        while q:
            #need to go through students and detect if a cycle exists
            curStudent = q.popleft()
            if curStudent == sandwiches[0]:
                sandwiches.pop(0)
                res -= 1
                cycleDetector = len(students)
                cycle = 0
            else:
                q.append(curStudent)
                cycle +=1
            if cycle >= cycleDetector:
                break

        return res