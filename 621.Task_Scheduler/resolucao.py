from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        # contar a frequência de cada tarefa
        task_counts = Counter(tasks)
        
        #encontrar a frequência maxima
        max_freq = 0
        for count in task_counts.values():
            max_freq = max(max_freq, count)
            
        # encontrar quantas tarefas têm essa frequência máxima
        num_max_freq_tasks = 0
        for count in task_counts.values():
            if count == max_freq:
                num_max_freq_tasks += 1
                
        # calcular o tempo com base nos ociosos
        time_with_idles = (max_freq - 1) * (n + 1) + num_max_freq_tasks
        
        return max(len(tasks), time_with_idles)
