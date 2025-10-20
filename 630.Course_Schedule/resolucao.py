import heapq

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        # organiza por deadline
        courses.sort(key=lambda x: x[1])
        
        max_heap = []
        current_time = 0
        
        # for nos cursos organizados
        for duration, lastDay in courses:
            if current_time + duration <= lastDay:
                current_time += duration
                heapq.heappush(max_heap, -duration)
            elif max_heap and -max_heap[0] > duration:
                # troca o curso atual com o de maior duraçao  ate agora
                current_time += duration - (-heapq.heappop(max_heap))
                heapq.heappush(max_heap, -duration)
                
        return len(max_heap)
