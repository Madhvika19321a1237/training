class Solution(object):
	    def getImportance(self, employees, id):
	        
	        if not employees: return
	        
	        empImportance = {}
	        for employee in employees:
	            empImportance[employee.id] = (employee.importance, employee.subordinates)
	            
	    
	        total = empImportance[id][0]
	       
	        s = [x for x in empImportance[id][1]]
	        seen = set()
	        while s:
	            nxt = s.pop()
	            if nxt not in seen:
	                total += empImportance[nxt][0]
	                for subordinate in empImportance[nxt][1]:
	                    if subordinate not in seen:
	                        s.append(subordinate)
	                seen.add(nxt)
	        
	        return total
	            
