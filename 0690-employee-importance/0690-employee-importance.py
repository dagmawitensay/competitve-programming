"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total_importance = 0
        def getChild(id):
            for employee in employees:
                if employee.id == id:
                    return employee
                
        def dfs(node):
            nonlocal total_importance
            if not node:
                return
            
            total_importance += node.importance
            
            for subordinate in node.subordinates:
                curr = getChild(subordinate)
                dfs(curr)
        
        start = getChild(id)
        
        dfs(start)
        return total_importance